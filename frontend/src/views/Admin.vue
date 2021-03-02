<template>
    <v-app>
        <v-app-bar
        dense
        dark
        fixed
        >
        <v-tabs centered fixed-tabs>
            <v-tab>Admin</v-tab>
        </v-tabs>
        </v-app-bar>

        <v-form class="mt-15">
        <v-container>
        <v-card
        v-if="!authenticated"
        class="mx-2 mb-5 mt-5"
        color="grey lighten-3"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        raised
        >
        <v-row justify="center">
            <v-col
            cols="12"
            md="4"
            >
            <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                outlined
                solo
                required
            ></v-text-field>
            </v-col>

            <v-col
            cols="12"
            md="4"
            >
            <v-text-field
                v-model="password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[passwordRules.required, passwordRules.min]"
                :type="show ? 'text' : 'password'"
                label="Password"
                hint="At least 8 characters"
                counter
                @click:append="show = !show"
                outlined
                solo
            ></v-text-field>
            </v-col>
        </v-row>

        <v-row justify="center">
            <v-btn
            class="mb-4"
            @click="validate"
            >
            Submit
            </v-btn>
        </v-row>
        </v-card>
         <v-btn
        v-if="authenticated"
        elevation="2"
        justify="center"
        @click="importProjects"
        >
        Import projects from GitHub
        </v-btn>
        </v-container>
        </v-form>
    </v-app>
</template>

<script>
import { mapState } from "vuex"

export default {

    data () {
        return {
            valid: true,
            show: false,
            password: '',
            passwordRules: {
                required: value => !!value || 'Required.',
                min: v => v.length >= 8 || 'Min 8 characters',
            },
            email: '',
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+/.test(v) || 'E-mail must be valid',
            ],
        }
    },
    methods: {
        validate () {
            let payload = {
                email: this.email,
                password: this.password,
            }
            this.$store.dispatch('checkUser', payload);
        },
        importProjects () {
            this.$store.dispatch('importGithubProjects');
        }
    },
    computed: {
        ...mapState({
            authenticated: "auth",
        })
    }
}
</script>