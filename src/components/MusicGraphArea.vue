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
            chart_width: 800,
            chart_height: 520,
            chart_margin:  { "top": 40, "bottom": 80, "right": 40, "left": 80 }
        };
    },
    mounted() {
        this.preprocess();
        this.drawChart();
    },
    methods: {
        preprocess(){

            d3.selectAll('svg > *').remove()
            d3.selectAll('svg').remove()
            this.svg = d3.select('#chart')
                        .append('svg')
                        .attr('width', this.chart_width)
                        .attr('height', this.chart_height)
                        .attr('class', "chart")

            this.musicInfos.forEach((element, idx) => {
                element['music_idx'] = idx;
                this.plot_data.push(element);
            });
        },
        drawChart(){
            const xScale = d3.scaleLinear()
            .domain([0, 1])
            .range([this.chart_margin.left, this.chart_width - this.chart_margin.right]);

            const yScale = d3.scaleLinear()
            .domain([0, 1])
            .range([this.chart_height - this.chart_margin.bottom, this.chart_margin.top]);

            // 軸の表示
            var axisx = d3.axisBottom(xScale).ticks(5);
            var axisy = d3.axisLeft(yScale).ticks(5);

            this.svg.append("g")
                .attr("transform", "translate(" + 0 + "," + (this.chart_height - this.chart_margin.bottom) + ")")
                .call(axisx)
                .append("text")
                .attr("fill", "black")
                .attr("x", (this.chart_width - this.chart_margin.left - this.chart_margin.right) / 2 + this.chart_margin.left)
                .attr("y", 50)
                .attr("text-anchor", "middle")
                .attr("font-size", "12pt")
                .attr("font-weight", "middle")
                .text("sad ↔️ happy");

            this.svg.append("g")
            .attr("transform", "translate(" + this.chart_margin.left + "," + 0 + ")")
            .call(axisy)
            .append("text")
            .attr("fill", "black")
            .attr("x", -(this.chart_height - this.chart_margin.top - this.chart_margin.bottom) / 2 - this.chart_margin.top)
            .attr("text-anchor", "middle")
            .attr("y", -50)
            .attr("transform", "rotate(-90)")
            .attr("font-weight", "middle")
            .attr("font-size", "12pt")
            .text("relax ↔️ excite");

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

                })
                .on('mouseover', function () { 
                    d3.select(this).style("cursor", "pointer").style("opacity", 0.8).style("r", "10px");
                })
                .on('mouseout', function(){
                    d3.select(this).style("opacity", 1).style("r", "8px");
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


