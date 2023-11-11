<template>
    <nav class="navbar" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
      <div class="navbar-brand">
        <router-link class="navbar-item is-size-4" to="/">EdumPass</router-link>
        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" @click="toggleNavbar" style="font-size: 30px;">
            ☰
        </a>
        


      </div>
  
      <div :class="['navbar-menu', { 'is-active': isNavbarActive }]">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item">Home</router-link>
          <router-link to="/about" class="navbar-item">About</router-link>
          <router-link to="/courses" class="navbar-item">Courses</router-link>
          <router-link to="/projects" class="navbar-item">Projects</router-link>
        </div>
  
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.user.isAuthenticated">
                <router-link to="/dashboard/create-course" class="button is-primary">Create course</router-link>
                <router-link to="/dashboard/my-account" class="button is-info">My account</router-link>
              </template>
  
              <template v-else>
                <router-link to="/sign-up" class="button is-primary"><strong>Sign up</strong></router-link>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isNavbarActive: false,
      };
    },
    methods: {
      toggleNavbar() {
        this.isNavbarActive = !this.isNavbarActive;
      },
    },
  };
  </script>
  