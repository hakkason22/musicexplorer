<template>
  <Main>
    <Header @artist_name='target_artist_name = $event' />
    <h1>{{ target_artist_name }}</h1>
    <h1 v-if="target_artist_name != ''">テストだよーーーーーん</h1>
  </Main>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  data(){
    return {
      target_artist_name: ""
    };
  }
})
</script>
