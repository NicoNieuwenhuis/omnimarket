<template>

    <li>
        <!--parent-->
        <a :class="{active: node.id === categoryId}" v-if="isFolder" href="javascript:" @click="toggle">
            <nuxt-link :to="`/categories/${node.slug}-${node.id}/`">
              <span class="fa fa-fw" :class="icon"></span> {{node.name}}
            </nuxt-link>
        </a>
        <!--if not folding, we do not need an binding event-->
        <a v-else href="javascript:" :title="node.name" :class="{active: node.id === categoryId}" @click="filterByCategory(node.id)">
          <nuxt-link :to="`/categories/${node.slug}-${node.id}/`">
            <span class="fa fa-fw fa-circle-o"></span> {{node.name}}
          </nuxt-link>
        </a>
        <!--children-->
        <ul v-if="isFolder" :class="isShow">
            <node v-for="child in node.children" :node="child" :search="search" :category="categoryId"></node>
        </ul>
    </li>
</template>

<script>
export default {
  name: "node",
  props: ['node', 'category', 'search'],
  data() {
    return {
      open: false,
      categoryId: this.category
    }
  },
  mounted() {
    let isNodeOpen = (d) => d.id === this.categoryId || d.children && d.children.some(isNodeOpen);
    this.open = isNodeOpen(this.node);
  },
  computed: {
    icon() {
      return {
        'fa-plus': !this.open,
        'fa-minus': this.open,
      }
    },
    isFolder() {
      return this.node.children && this.node.children.length
    },
    isShow() {
      return this.open ? 'show' : 'hide'
    }
  },
  methods: {
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
  display: block;
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