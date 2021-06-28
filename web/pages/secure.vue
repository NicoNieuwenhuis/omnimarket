<template>
    <div>
        <b-alert show variant="warning">
            This is a secure page!
        </b-alert>
        <b-row>
            <p  v-if="this.$auth.user.is_staff === true">
      staff
    </p>
            <b-col md="8">
                <b-card title="State">
                    <pre>{{ state }}</pre>
                </b-card>
            </b-col>
            <b-col md="4">
                <b-card title="Scopes" class="mb-2">
                    User:
                    <b-badge>{{ $auth.hasScope('admin') }}</b-badge>
                    is_staff:
                    <b-badge>{{ this.$auth.hasScope('is_staff') }}</b-badge>
                    Admin:
                    <b-badge>{{ this.$auth.hasScope('admin') }}</b-badge>
                </b-card>
            </b-col>
        </b-row>
        <hr>
        <b-btn-group>
            <b-button @click="$auth.fetchUser()">
                Fetch User
            </b-button>
            <b-button @click="$auth.logout()">
                Logout
            </b-button>
        </b-btn-group>
    </div>
</template>

<script>
export default {
    middleware: ['auth'],
    computed: {
        state () {
            return JSON.stringify(this.$auth.$state, undefined, 2)
        }
    }
}
</script>
