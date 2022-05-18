<template>
  <div class="chart_wrapper">
    <div id="chart" class="chart_area">
    </div>
    <div class="player_wrapper">
        <span v-on:click="target_music_idx = 'aaa'" id="test_dom">{{ target_music_idx }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import * as d3 from 'd3'

import Vue from 'vue'
export default Vue.extend({
    props: ["musicInfos"],
    data(){
        return {
            svg: null,
            target_music_idx: "tes",
            plot_data: [],
        };
    },
    mounted() {
        this.preprocess();
        this.drawChart();
    },
    methods: {
        preprocess(){
            console.log(document.body.clientWidth);
            const width = document.body.clientWidth * 0.8;

            d3.selectAll('svg > *').remove()
            d3.selectAll('svg').remove()
            this.svg = d3.select('#chart')
                        .append('svg')
                        .attr('width', width)
                        .attr('height', 520)
                        .attr('class', "chart")

            this.musicInfos.forEach((element, idx) => {
                element['music_idx'] = idx;
                this.plot_data.push(element);
            });
        },
        drawChart(){
            const xScale = d3.scaleLinear()
            .domain([0, 1])
            .range([30, 1180]);

            const yScale = d3.scaleLinear()
            .domain([0, 1])
            .range([30, 500]);

            this.svg.append("g")
                .selectAll("circle")
                .data(this.plot_data)
                .enter()
                .append("circle")
                .attr("cx", function(d) { return xScale(d['valence']); })
                .attr("cy", function(d) { return yScale(d['arousal']); })
                .attr("id", function(d) { return d['music_url']; })
                .attr("fill", "#40e0d0")
                .attr("r", "8px")
                .on('click', function (data) { 
                    let music_url = data.target.id;
                    
                    let el = document.getElementById("test_dom");
                    el.innerHTML = "<h1>" + music_url + "</h1>";

                });

            // ラベルの表示
            this.svg.append("g")
                .selectAll("circle")
                .data(this.plot_data)
                .enter()
                .append("text")
                .attr("x", function(d) { return xScale(d['valence']); })
                .attr("y", function(d,) { return yScale(d['arousal']); })
                .text(function(d){ return d['music_name'];})
                .attr("dy", "-18px")
                .attr("fill", "#999999")
                .attr("font-size", "12px")
                .attr('text-anchor', "middle"); 
        },
    },
})
</script>
<style scoped>

    .chart_area{     
        padding: 30px;
        margin: 0 auto;
    }

    .player_wrapper{
        border: 2px solid black;
        border-radius: 30px;
        width:40%;
        position: absolute;
        bottom: 2;
        left: 0;
        right: 0;
        margin: auto;
    }
</style>


