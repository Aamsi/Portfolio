<template>
  <v-app>
    <div>
    <v-app-bar dense dark>
    <v-tabs centered fixed-tabs>
        <v-tab to="/projects">Mes projets</v-tab>
        <v-tab to="/about">À propos de moi</v-tab>
    </v-tabs>
    </v-app-bar>
  </div>
  <router-view />




  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    //
  }),
};
</script>
