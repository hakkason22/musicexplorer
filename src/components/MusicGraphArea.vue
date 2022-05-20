<template>
  <div class="chart_wrapper">
    <div id="chart" class="chart_area">
    </div>
    <div class="player_wrapper" id="player_wrapper"></div>
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
            valence_range: {},
            energy_range: {},
            plot_data: [],
            chart_width: 1300,
            chart_height: 1020,
            chart_margin:  { "top": 40, "bottom": 80, "right": 40, "left": 80 }
        };
    },
    mounted() {
        this.preprocess();
        this.drawChart();
    },
    watch:{
        musicInfos: function(){
            let chart_svg = document.getElementById('chart_svg');
            let chart_svg_parent = chart_svg.parentNode;
            this.plot_data = [];
            this.svg = null;
            chart_svg_parent.removeChild(chart_svg);
            this.preprocess();
            this.drawChart();
        }
    },
    methods: {
        preprocess(){
            this.svg = d3.select('#chart')
                        .append('svg')
                        .attr('width', this.chart_width)
                        .attr('height', this.chart_height)
                        .attr('id', "chart_svg")

            let valence_list:number[] = [];
            let energy_list = [];
            this.musicInfos.forEach((element, idx) => {
                element['music_idx'] = idx;
                this.plot_data.push(element);
                valence_list.push(element['valence']);
                energy_list.push(element['energy']);
            });
            this.valence_range['max'] = Math.max(...valence_list);
            this.valence_range['min'] = Math.min(...valence_list);
            this.energy_range['max'] = Math.max(...energy_list);
            this.energy_range['min'] = Math.min(...energy_list);
        },
        drawChart(){
            const xScale = d3.scaleLinear()
            .domain([this.valence_range['min'], this.valence_range['max']])
            .range([this.chart_margin.left, this.chart_width - this.chart_margin.right]);

            const yScale = d3.scaleLinear()
            .domain([this.energy_range['min'], this.energy_range['max']])
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
                .attr("cy", function(d) { return yScale(d['energy']); })
                .attr("id", function(d) { return d['music_id']; })
                .attr("fill", "#40e0d0")
                .attr("r", "5px")
                .on('click', function (data) { 
                    let music_id = data.target.id;
                    
                    let el = document.getElementById("player_wrapper");
                    el.innerHTML = '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/'
                            + music_id
                            + '?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>';

                })
                .on('mouseover', function () { 
                    d3.select(this).style("cursor", "pointer").style("opacity", 0.8).style("r", "10px");
                })
                .on('mouseout', function(){
                    d3.select(this).style("opacity", 1).style("r", "5px");
                });

            // ラベルの表示
            this.svg.append("g")
                .selectAll("circle")
                .data(this.plot_data)
                .enter()
                .append("text")
                .attr("x", function(d) { return xScale(d['valence']); })
                .attr("y", function(d,) { return yScale(d['energy']); })
                .text(function(d){ return d['music_name'];})
                .attr("dx", "15px")
                .attr("dy", "-5px")
                .attr("fill", "black")
                .attr("font-size", "10px")
                .attr('text-anchor', "middle")
                .style('pointer-events', 'none'); 
        },
    },
})
</script>
<style scoped>

    .chart_wrapper{
        padding-bottom:60px;
    }

    .chart_area{     
        padding: 30px;
        margin: 0 auto;
        text-align: center;
       
    }

    .player_wrapper{
        width: 40%;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        margin: auto;
    }
</style>


