<template>
    <div class="login_induction_wrapper">
        <h2>ログイン</h2>
        <div class="link_field" @click="googleLogin">
            <div class="google_icon_area">
                <img src="../../images/google-icon.svg" alt="">
            </div>
            <div class="link_area">
                <span>
                    Googleアカウントでログイン
                </span>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    methods: {
        googleLogin: function(err: any) {
            this.$store
                .dispatch('signInWithGoogle')
                .then(() => {
                    location.reload()
                })
                .catch((err: any) => {
                    alert('現在Googleでのログインは使用できません。後ほどお試しください。')
                    location.reload()
                })
        },
    }
})
</script>
<style scoped>
    .login_induction_wrapper{
        position: relative;
    }
    .link_field{
        text-align: center;
        background: lightgray;
        border-radius: 10px;
        color: black;
        display: flex;
        justify-content: center;
        align-items: center;
        width: fit-content;
        padding: 10px 20px;
        margin: 0 auto;
        cursor: pointer;
    }
    .link_field:hover {
        opacity: 0.9;
    }
    .link_field span {
        font-size: 26px;
        padding: 5px 30px;
    }
    .google_icon_area {
        width: fit-content;
    }
    .google_icon_area img{
        width: 50px;
    }
</style>
