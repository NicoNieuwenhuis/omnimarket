<template>
    <div class="profile-page">
        <section class="section-profile-cover section-shaped my-0">
            <div class="shape shape-style-1 shape-primary alpha-4">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </section>
        <section class="section section-skew">
            <div class="container">
                <card shadow class="card-profile mt--300" no-body>
                    <div class="px-4">
                        <div class="row justify-content-center">
                            <div class="col-lg-3 order-lg-2">
                                <div class="card-profile-image">
                                        <img :src="users.profilepic">
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-3 text-lg-right align-self-lg-center">
                                <div class="card-profile-actions py-4 mt-lg-0">
                                              <nuxt-link :to="`/user/${users.slug}/edit`">
                                                <div v-if="$auth.$state.loggedIn">
                                                  <base-button v-if="author" type="default" class="float-left">Edit</base-button>
                                                </div>
                                              </nuxt-link>
                                    <base-button type="default" class="float-right">Message</base-button>
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-1">
                                <div class="card-profile-stats d-flex justify-content-center">
                                  <div>
                                    <h3>member since</h3>
                                    <p>{{users.member_since}}</p>
                                  </div>
                                </div>
                            </div>
                        </div>
                        <div class="mt-5 py-5 border-top text-center">
                            <div class="row justify-content-center">
                                <div class="col-lg-9">
                                    <p>{{users.about_you}}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </card>
            </div>
        </section>
    </div>
</template>

<script>
export default {
  auth: false,
  middleware: ['auth'],
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        },
        admin() {
            return this.users.admin === true;
        },
        author() {
            return this.$auth.user.username == this.users.username;
        },
    },
    head(){
        return{
            title: 'view users'
        }
    },
    data(){
        return{
            users: []
        }
    },
    async asyncData({$axios, params}) {
        try{
            let users = await $axios.$get(`/server/user/${params.slug}/`)
            console.log(users)
            return{ users }
        } catch{}
            console.log()
    },
  methods: {
    async submitListings({$axios, users}) {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.users) {
        formData.append(data, users[data]);
      }
      try {
        let response = await this.$axios.$post("/server/user/${users.slug}/", formData, config);
        this.$router.push("/users/");
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>

<style>
.section-profile-cover {
    height: 446px;
}
.profile-page .card-profile {
    margin-top: -300px;
}
</style>