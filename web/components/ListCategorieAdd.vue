<template>

    <li>
        <!--parent-->
        <a :class="{active: list.id === categoryId}" v-if="isFolder" href="javascript:" @click="toggle" v-on:click="setdata(list)">
          <span class="fa fa-fw" :class="icon"></span>
            {{list.name}}
        </a>
        <!--if not folding, we do not need an binding event-->
        <a v-else v-on:click="setdata(list)" :title="list.name" :class="{active: list.id === categoryId}" >
          <span  class="fa fa-fw fa-circle-o"></span>
            {{list.name}}
        </a>
        <!--children-->
        <ul v-if="isFolder" :class="isShow" >
            <list v-on:click="setdata(list)" v-for="list in list.children" :list="list" :category="categoryId"></list>
        </ul>
    </li>
</template>

<script>
export default {
  name: "list",
  props: ['list', 'category', 'selected'],
  data() {
    return {
      open: false,
      categoryId: this.category
    }
  },
  mounted() {
    let isNodeOpen = (d) => d.id === this.categoryId || d.children && d.children.some(isNodeOpen);
    this.open = isNodeOpen(this.list);
  },
  computed: {
    icon() {
      return {
        'fa-plus': !this.open,
        'fa-minus': this.open,
      }
    },
    isFolder() {
      return this.list.children && this.list.children.length
    },
    isShow() {
      return this.open ? 'show' : 'hide'
    }
  },
  methods: {
      setdata: function(list) {
            this.$emit('clicked', list.id)
        },
    toggle() {
      this.open = !this.open
    },
    filterByCategory(id) {
      this.categoryId = id
    }
  }
};
</script>

<style>
.active {
  background-color: #eeeeee;
}

.pd-search-filter > .panel-body ul.filter-category {
  padding-left: 0;
  list-style: none;
  margin: 0 -15px 0;
}

.pd-search-filter > .panel-body ul.filter-category > li a {
    display: inline-table;
    padding: 10px 15px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.pd-search-filter > .panel-body ul.filter-category > li a:last-child {
  padding-left: 45px;
}

.pd-search-filter > .panel-body ul.filter-category > li a:focus, .pd-search-filter > .panel-body ul.filter-category > li a:hover {
  background-color: #eeeeee;
  text-decoration: none;
}

.pd-search-filter > .panel-body ul.filter-category > li a + ul {
  padding-left: 0;
  list-style: none;
}

.pd-search-filter > .panel-body ul.filter-category > li a + ul > li > a {
  padding-left: 30px;
}

.show {
  display: block !important;
}

.hide {
  display: none !important;
}
</style>