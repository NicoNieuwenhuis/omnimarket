<template>
    <div v-if="admin">
        <div class="container page" >
            <div class="row" >
            <div class="col-xs-12 col-md-3">
                <div class="sidebar">
                    <p>Menu</p>
                <row></row>
                    <p>Dashboard</p>
                <row></row>
                    <p>Listings</p>
                    <p>Users</p>
                    <p>Messages</p>
                    <p>Reviews</p>
                    <p>Transactions</p>
                <row></row>
                    <p>Theme</p>
                    <p>Settings</p>
                    <a href="/admin/categories">Categories</a>

                </div>
            </div>
            <b-container class="col-xs-12 col-md-9">
                <div class="row" >
                </div>
            </b-container>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    middleware: ['auth'],
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        },
        admin() {
            return this.$auth.user.admin === true;
        },
    }
}
</script>
