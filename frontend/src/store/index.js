import Vue from "vue"
import Vuex from "vuex"
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(Vuex)
Vue.use(VueAxios, axios)

Vue.axios.defaults.baseURL = "http://localhost:3080/";

export default new Vuex.Store({
    state: {
        categories: ['Tous'],
        projects: [],
        auth: false,
    },
    mutations: {
        SAVE_PROJECTS(state, projects) {
            state.projects = [];
            for (let project of projects) {
                if (!project.picture) {
                    project.picture = {
                        source:  `${process.env.BASE_URL}default_1.png`,
                        alt: 'Photo de projet'
                    };
                } else {
                    project.picture = {
                        source: `${process.env.BASE_URL}${project.picture}`,
                        alt: 'Photo de projet'
                    }
                }
                if (!project.description)
                    project.description = "Aucune description pour le moment";
                if (project.categories.length == 0)
                    project.categories.push('Tous')
                state.projects.push(project);
            }
        },
        SAVE_CATEGORIES(state, categories) {
            for (var category of categories)
                state.categories.push(category.name);
        },
        AUTHENTICATE(state, data) {
            if (data.email)
                state.auth = true;
        }
    },
    actions: {
        loadCategories({ commit }) {
            Vue.axios.get('categories/')
            .then(response => {
                commit('SAVE_CATEGORIES', response.data);
            })
            .catch(error => {
                throw new Error(`API${error}`);
            });
        },
        loadProjects({ commit }) {
            Vue.axios.get('projects/')
            .then(response => {
                commit('SAVE_PROJECTS', response.data);
            })
            .catch(error => {
                throw new Error(`API${error}`);
            });
        },
        checkUser({ commit }, payload) {
            let formData = new FormData();
            formData.append('email', payload.email);
            formData.append('password', payload.password);

            Vue.axios.post('admin/login', formData)
            .then(response => {
                commit('AUTHENTICATE', response.data)
            })
            .catch(error => {
                throw new Error (`API${error}`);
            });
        },
        importGithubProjects({ commit }) {
            Vue.axios.get('projects/github')
            .then(response => {
                commit('SAVE_PROJECTS', response.data);
            })
            .catch(error => {
                throw new Error(`API${error}`);
            });
        }
    }
})