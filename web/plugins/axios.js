await $axios.onRequest((config) => {
    config.headers.common['Content-Type'] = 'application/json'
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'X-CSRFToken'
    const csrfCookie = app.$cookies.get('csrftoken')
    config.headers.common['X-CSRFToken'] = csrfCookie
    console.log(config)