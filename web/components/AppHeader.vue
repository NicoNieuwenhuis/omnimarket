<template>
    <header class="header-global">
        <base-nav class="navbar-main" type="" transparent effect="dark" expand>
            <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
                Estuaries
            </router-link>

            <div class="row" slot="content-header" slot-scope="{closeMenu}">
                <div class="col-6 collapse-brand">
                    <a href="/">
                        Estuaries
                    </a>
                </div>
                <div class="col-6 collapse-close">
                    <close-button @click="closeMenu"></close-button>
                </div>
            </div>
            <ul class="navbar-nav  navbar-nav-hover ml-lg-auto">
                <base class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="/listings/add" class="nav-link">
                        <button type="button" class="btn btn-warning">Add Listing</button>
                    </a>
                   <template v-if="$auth.$state.loggedIn">
                <base-dropdown tag="li" class="nav-item">
                    <a slot="title" class="nav-link" data-toggle="dropdown" role="button">

                        <i v-if="newmessage" class="newmessage ni ni-active-40"></i>
                        <fa icon="envelope-open-text"></fa>
                        <vue-letter-avatar :name="$auth.user.username" size='40' :rounded=true />
                    </a>
                    <button class="dropdown-item" @click=$auth.logout()>Logout</button>
                    <router-link :to="'/users/' + $auth.user.username" class="dropdown-item">Profile</router-link>
                </base-dropdown>
                    <a v-if="admin" slot="admin" href="/admin" class="nav-link">
                        <button type="button" class="btn btn-warning">Admin</button>
                    </a>
                    </template>
                    <template v-else>
                <base class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="/login" class="nav-link">
                        <i class="ni ni-ui-04 d-lg-none"></i>
                        <span>Log in</span>
                    </a>
                </base>
                <base class="nav-item" menu-classes="dropdown-menu-xl">
                    <a slot="title" href="/register" class="nav-link">
                        <i class="ni ni-ui-04 d-lg-none"></i>
                        <span>Register</span>
                    </a>
                </base>
              </template>
            </ul>
        </base-nav>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";
import VueLetterAvatar from 'vue-letter-avatar';
import Vue from 'vue';

Vue.use(VueLetterAvatar);

export default {
  middleware: ['auth'],
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        },
        admin() {
            return this.$auth.user.admin === true;
        },
        newmessage() {
            return this.$auth.user.new === true;
        },
    },
    components: {
        BaseNav,
        CloseButton,
        BaseDropdown
    }
};
</script>

<style>
.navbar-main {
    height: 65px;
}
.nav-link {
    line-height: 35px;
}
i.newmessage.ni.ni-active-40 {
    position: absolute;
    transform: rotate(35deg);
    top: 39px;
    right: 25px;
    background-color: #172b4d;
    color: #fff;
    padding: 5px;
    border-radius: 50%;
}
</style>
