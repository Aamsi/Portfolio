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
        projects: []
    },
    mutations: {
        SAVE_PROJECTS(state, projects) {
            state.projects = [];
            for (let project of projects) {
                if (!project.picture) {
                    project.picture = {
                        source:  'https://picsum.photos/seed/picsum/300/300',
                        alt: 'Photo de projet'
                    };
                }
                state.projects.push(project);
            }
        },
        SAVE_CATEGORIES(state, categories) {
            for (var category of categories)
                state.categories.push(category.name);
        },
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
    }
})