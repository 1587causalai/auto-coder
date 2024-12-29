window.$docsify = {
  name: 'AutoCoder',
  repo: 'https://github.com/qian-bi/auto-coder',
  loadSidebar: true,
  subMaxLevel: 3,
  search: {
    paths: 'auto',
    placeholder: '搜索',
    noData: '没有找到结果',
    depth: 6
  },
  copyCode: {
    buttonText: '复制',
    errorText: '错误',
    successText: '已复制'
  },
  auto2top: true,
  coverpage: false,
  executeScript: true,
  mergeNavbar: true,
  formatUpdated: '{MM}/{DD} {HH}:{mm}',
  plugins: [
    function(hook, vm) {
      hook.beforeEach(function(html) {
        return html + '\n\n----\n\n' +
          '> 最后更新时间: {docsify-updated} ' +
          '由 [AutoCoder](https://github.com/qian-bi/auto-coder) 强力驱动';
      });
    }
  ]
}; 