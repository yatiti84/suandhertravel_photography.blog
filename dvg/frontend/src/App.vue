<template>
  <div id="app">
    <header>
      <navbarMenu></navbarMenu>
      <h1>雨女攝影旅遊suanddhertravel Blog</h1>
      <div class="route">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/about" class="nav-link">About</router-link>
        <router-link to="/AllPosts" class="nav-link">allposts</router-link>
      </div>
    </header>
    <nav>
      <router-view />
    </nav>
  </div>
</template>

<style>
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Noto Serif', 'Noto Sans', 'Source Han Sans', 'Microsoft YaHei', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
a {
    color:#634D32;
    text-decoration: none;
    font-weight: bold;
}
.route .nav-link {
  margin-right: 50px; 
  }
</style>
<script>
import navbarMenu from '@/components/navbarMenu.vue';
export default {
  name: 'App',
  components: {
    navbarMenu,
  },
}
</script >