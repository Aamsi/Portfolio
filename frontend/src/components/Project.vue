<template>
    <v-card
    class="mx-1"
    max-width="60%%"
    min-width="350"
    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
    dark
    hover
    raised
  >
    <v-img
      :src="image.source"
      :alt="image.alt"
      white
      height="180"
    ></v-img>

    <v-card-title>
      {{ title }}
    </v-card-title>

    <v-card-subtitle>
      {{ generateShortDescription }}
    </v-card-subtitle>

    <v-card-actions>
      <v-btn
        color="dark lighten-2"
        text
        :href="url"
        target='_blank'
      >
        Repository
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          {{ description }}
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
    name: 'Project',
    props: {
        image: {
            type: Object,
            required: false,
        },
        title: {
            type: String,
            required: true,
        },
        description: {
            type: String,
            required: true,
        },
        url: {
            type: URL,
            required: true
        },
    },
    data() {
        return {
            short_description: "En cours...",
            show: false,
        }
    },
    computed: {
        generateShortDescription() {
            let short_description = this.description.substring(0, 15) + '...';
            if (!short_description)
                return "En cours...";
            return short_description;
        },
    }
}
</script>
