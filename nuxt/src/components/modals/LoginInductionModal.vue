<template>
    <div class="login_induction_wrapper">
        <h2>お気に入り機能を使用するためにはログインが必要です</h2>
        <div class="link_field">
            <span @click="toLoginPage">ログインページへ</span>
        </div>
    </div>
</template>
<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
    methods:{
        toLoginPage() {
            this.$router.push('/login');
        }
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
