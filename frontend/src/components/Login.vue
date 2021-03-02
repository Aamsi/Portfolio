<template>
    <v-card
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
</template>