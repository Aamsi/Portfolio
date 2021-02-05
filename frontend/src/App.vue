<template>
  <v-app>
    <div>
    <v-app-bar dense dark>
    <v-tabs centered fixed-tabs>
        <v-tab to="/projects">Mes projets</v-tab>
        <v-tab to="/about">À propos de moi</v-tab>
    </v-tabs>
    </v-app-bar>
    <router-view />
    </div>

    <v-footer
    dark
    padless
    fixed
    >
      <v-card
      class="flex text-center"
      flat
      tile
      >
        <v-btn
        v-for="icon in icons"
        :key="icon"
        class="mx-4"
        dark
        icon
        centered
        :href="icon.url"
        target="_blank"
        >
        <v-icon size="24px"> {{ icon.name }} </v-icon>
        </v-btn>
        <v-card-text class="py-2 white--text text-center">
          {{ new Date().getFullYear() }} — <strong>OUALI Ismael</strong>
        </v-card-text>
      </v-card>
    </v-footer>

  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    icons: [
      {
        name: 'mdi-linkedin',
        url: 'https://www.linkedin.com/in/isma%C3%ABl-ouali-86b3a3192/'
      },
      {
        name: 'mdi-github',
        url: 'https://github.com/Aamsi'
      }
    ]
  }),
};
</script>
