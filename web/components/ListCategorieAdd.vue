<template>
<div>
<div  v-for="node in nondes">

{{node.name}}
</div>
</div>
</template>

<script>
export default {
  name: "node",
  props: ['node', 'nodes'],
  data() {
    return {
      open: false,
      selected: []
    }
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
    },
    setSelected: function() {
      if (this.selected.length > 0 && this.selected[0].id == this.node.id)
        return true;
      else
        return false;
    }
  },
  methods: {
    toggle() {
      this.open = !this.open
    },
    selectNode (node) {
      this.selected = [];
      this.selected.push({
        'id': this.node.id,
        'pricetype': this.node.pricetype,
      });
      this.$emit('nodeSelect', node)
    },
    nodeSelect(selected) {

      this.$emit('nodeSelect', node)

    },
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