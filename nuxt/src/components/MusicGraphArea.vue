<template>
  <div class="chart_wrapper" :class="chart_cursor">
    <svg
        @mousedown="startPan"
        @mousemove="panning"
        @mouseup="endPan"
        @mouseleave="endPan"
        @wheel="zoomGraph"
        :viewBox="viewbox" 
        :width=svg_width
        :height=svg_height
    >
        <text v-for="musicInfo in musicInfos" :key="musicInfo.music_id"
                :x="musicInfo['valence'] * (svg_width-100) + 100 - svg_min_width"
                :y="(1 - musicInfo['energy']) * (svg_height-100) + 100 -svg_min_height"
                :fill="musicInfo['graph_color']"
                @click="displayDetail(musicInfo)"
                :font-size="chart_font_size"
                class="graph_element"
        >{{ musicInfo.display_music_name }}</text>
    </svg>
    <MusicPlayer v-if="$store.state.player.target_music_id !== ''"
        @setFavoriteMusicInfo="setFavoriteMusicInfo"
    />
  </div>
</template>

<script lang="ts">
import axios from 'axios'
import Vue from 'vue'
import { Music } from '../pages/index.vue'
import MusicPlayer from './MusicPlayer.vue';

export default Vue.extend({
    props: ["musicInfos", "artistName"],
    data() {
        return {
            svg_width: 1000,
            svg_height: 1000,
            svg_min_width: 0,
            svg_min_height: 0,
            chart_width: 300,
            chart_height: 220,
            chart_min_width: 0,
            chart_min_height: 0,
            chart_font_size: 14,
            normal_color: "#FFFEF9",
            favorite_color: "#00fa9a",
            playing_color: "#ff00ff",
            prev_point: { x: 0, y: 0 },
            is_panning: false,
            chart_cursor: "chart_grab"
        };
    },
    mounted() {
        this.preProcess();
        this.$nuxt.$on("addFavoriteToChart", this.addUpdateData);
    },
    watch: {
        artistName: function () {
            this.preProcess();
        }
    },
    computed: {
        viewbox: function (): string {
            return [this.chart_min_width, this.chart_min_height, this.chart_width, this.chart_height].join(" ");
        }
    },
    methods: {
        setup() {
            this.musicInfos.forEach((musicInfo: Music) => {
                if (musicInfo.music_name.length < 10) {
                    musicInfo.display_music_name = musicInfo.music_name;
                }
                else {
                    musicInfo.display_music_name = musicInfo.music_name.slice(0, 9) + "...";
                }
                // グラフの色を設定
                if (musicInfo.music_id == this.$store.state.player.target_music_id) {
                    musicInfo.graph_color = this.playing_color;
                }
                else if (musicInfo.is_favorite) {
                    musicInfo.graph_color = this.favorite_color;
                }
                else {
                    musicInfo.graph_color = this.normal_color;
                }
                if ("is_favorite" in musicInfo === false) {
                    musicInfo.is_favorite = false;
                }
            });
            this.musicInfos.splice();
        },
        preProcess() {
            this.setup();
            this.setFavoriteMusicInfo();
            this.setChartSize();
        },
        setChartSize() {
            this.chart_width = window.innerWidth;
            this.chart_height = window.innerHeight;
            this.chart_min_width = 0;
            this.chart_min_height = 0;
            this.svg_width = this.chart_width;
            this.svg_height = window.innerHeight * 0.91;
            this.svg_min_width = this.chart_min_width;
            this.svg_min_height = this.chart_min_height;
            this.chart_font_size = 14;
        },
        addUpdateData(targetMusicInfo: Music) {
            targetMusicInfo.is_favorite = true;
            this.musicInfos.push(targetMusicInfo);
            this.setup();
        },
        displayDetail(music: Music) {
            if ("is_favorite" in music === false) {
                music.is_favorite = false;
            }
            this.$store.commit("player/setMusic", music);
            this.setup();
            console.log(this.$store.state.player.target_music_name);
        },
        async setFavoriteMusicInfo() {
            const user_id: string = this.$store.getters.user.uid;
            const url: string = `${process.env.BACKEND_ROOT}/music/favorite/list`;
            const params: any = new URLSearchParams();
            params.append("user_id", user_id);
            const response = await axios.post(url, params);

            const favoriteMusicInfos: Array<Music> = response.data.data;
            let favorite_music_ids: Array<string> = [];
            favoriteMusicInfos.forEach((favoriteMusicInfo: Music) => {
                favorite_music_ids.push(favoriteMusicInfo.music_id);
            });
            this.musicInfos.forEach((musicInfo: Music) => {
                if (favorite_music_ids.includes(musicInfo.music_id)) {
                    musicInfo.is_favorite = true;
                } else{
                    musicInfo.is_favorite = false;
                }
            });
            this.setup();
        },
        startPan(event: any) {
            this.is_panning = true;
            this.chart_cursor = "chart_grabbing";
            this.prev_point = {
                x: event.offsetX,
                y: event.offsetY,
            };
        },
        endPan() {
            this.chart_cursor = "chart_grab";
            this.is_panning = false;
        },
        panning(event: any) {
            if (this.is_panning == false) {
                return;
            }
            let point = {
                x: event.offsetX - this.prev_point.x,
                y: event.offsetY - this.prev_point.y,
            };
            const pan_rate = 0.4;
            this.chart_min_width = this.chart_min_width - point.x * pan_rate;
            this.chart_min_height = this.chart_min_height - point.y * pan_rate;
            this.prev_point = {
                x: event.offsetX,
                y: event.offsetY
            };
        },
        zoomGraph(event: any) {
            event.preventDefault();
            const scale = Math.pow(1.05, event.wheelDelta < 0 ? 1 : -1);
            if (this.chart_height * scale < 0 || this.chart_width * scale >= this.svg_width) {
                return;
            }
            const point = {
                x: event.offsetX,
                y: event.offsetY,
            };
            const sx = point.x / this.svg_width;
            const sy = point.y / this.svg_height;
            const target_x = this.chart_min_width + this.chart_width * sx;
            const target_y = this.chart_min_height + this.chart_height * sy;
            this.chart_width = this.chart_width * scale;
            this.chart_height = this.chart_height * scale;
            this.chart_min_width = target_x + scale * (this.chart_min_width - target_x);
            this.chart_min_height = target_y + scale * (this.chart_min_height - target_y);
            this.chart_font_size *= scale;
        }
    },
    components: { MusicPlayer }
})
</script>
<style scoped>
    .chart_wrapper{
        text-align: center;
        user-select: none;
    }
    .chart_grab {
        cursor: grab;
    }
    .chart_grabbing {
        cursor: grabbing;
    }
    .graph_element{
        cursor: pointer !important;
        border: 1px solid white;
    }
    .graph_element:hover {
        opacity: 0.9;
    }
</style>


