<template>
    <div class="login_wrapper" @click="googleLogin">Googleアカウントでログイン！w</div>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    data: function() {
        return {
            error_msg: ""
        }
    },
    methods: {
        googleLogin: function(err: any) {
            this.$store
                .dispatch('signInWithGoogle')
                .then(() => {
                    this.$router.push({
                        name: 'index'
                    })
                })
                .catch((err: any) => {
                    this.error_msg =
                        '現在Googleでのログインは使用できません。後ほどお試しください。'
                })
        },
    }
})
</script>
<style scoped>
  .login_wrapper{
    background: lightblue;
    padding:20px;
    cursor: pointer;
  }
  .login_wrapper:hover{
    opacity: 0.8;
  }
</style>
