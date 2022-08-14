<template>
    <div class="login_induction_wrapper">
        <h2>ログイン</h2>
        <div class="link_field">
            <span @click="googleLogin">Googleアカウントを使用する</span>
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
        margin-top: 30%;
    }
    .link_field span {
        font-size: 24px;
        cursor: pointer;
        padding: 10px 15px;
        background: black;
        border-radius: 50px;
        color: white;
    }
</style>
