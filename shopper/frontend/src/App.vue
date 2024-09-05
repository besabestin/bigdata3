<script>
import { RouterLink, RouterView } from 'vue-router'

export default {
  setup (){
  },
}
</script>

<template>
  <header>
    <div class="container m-auto p-4">
      <div class="flex-container">
        <div class="site-title">
          <RouterLink to="/">
            <h1 class="text-3xl">Shopper</h1>
          </RouterLink>
        </div>
        <nav>
          <RouterLink to="/listings">Listings</RouterLink>
          <RouterLink to="/about">About</RouterLink>
        </nav>
      </div>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  /* max-height: 100vh; */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
header .wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1280px;
  margin: 0 auto;
}
.flex-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

nav {
  font-size: 12px;
  display: flex;
  gap: 1rem;
  align-items: center;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

</style>
