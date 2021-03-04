<template>
  <v-container class="mt-15">
    <p class="text-center">
    Âgé de 23 ans, j'ai été étudiant pendant 4 ans en Sciences pharmaceutique. Puis j'ai décidé de changer de voie et de commencer une formation de développeur d'application en Python.
    Depuis, en plus de la formation, j'ai pu étendre mes compétences en effectuant un stage en entreprise et plusieurs missions Freelance.
    Je suis aujourd'hui étudiant à 42 Paris et j'effectue toujours des missions à temps partiel.</p>
    <br/>
    <p class="text-center">
    Passionné d'informatique et de développement , je peux vous accompagner dans vos projets informatiques de développement web apps (Flask, Django, Jquery, VueJS...) et développement d'API REST.
    </p>
    <br/>
    <p class="text-center">
    Le métier de développeur est un métier d'apprentissage constant, et de défis à relever tous les jours. C'est ce qui m'a motivé à faire de ma passion mon job.
    Autodidacte et autonome, j'ai beaucoup appris via mes nombreux projets personnels mais aussi grâce aux différentes formations et expériences.
    Désireux d'élargir mon champ de compétences, je reste informé des nouvelles technologies.
    </p>

    <v-row
    justify="center"
    class="mt-5"
    >
      <v-img
      :src="profile_picture.source"
      :alt="profile_picture.alt"
      white
      max-width="35%"
      ></v-img>
    </v-row>

  </v-container>
</template>

<script>
export default {
    name: 'About',
    data () {
      return {
        profile_picture: {
          source: `${process.env.BASE_URL}me.png`,
          alt: "me"
        }
      }
    }
}
</script>