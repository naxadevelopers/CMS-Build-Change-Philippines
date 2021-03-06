// lazyload config
var baseurl = window.location.origin;
var jp_config = {
  easyPieChart:   [   baseurl+'/static/bower_components/jquery.easy-pie-chart/dist/jquery.easypiechart.fill.js'],
  sparkline:      [   baseurl+'/static/bower_components/jquery.sparkline/dist/jquery.sparkline.retina.js'],
  plot:           [   baseurl+'/static/bower_components/flot/jquery.flot.js',
                      baseurl+'/static/bower_components/flot/jquery.flot.pie.js',
                      baseurl+'/static/bower_components/flot/jquery.flot.resize.js',
                      baseurl+'/static/bower_components/flot.tooltip/js/jquery.flot.tooltip.js',
                      baseurl+'/static/bower_components/flot.orderbars/js/jquery.flot.orderBars.js',
                      baseurl+'/static/bower_components/flot-spline/js/jquery.flot.spline.js'],
  moment:         [   baseurl+'/static/bower_components/moment/moment.js'],
  screenfull:     [   baseurl+'/static/bower_components/screenfull/dist/screenfull.min.js'],
  slimScroll:     [   baseurl+'/static/bower_components/slimscroll/jquery.slimscroll.min.js'],
  sortable:       [   baseurl+'/static/bower_components/html5sortable/jquery.sortable.js'],
  nestable:       [   baseurl+'/static/bower_components/nestable/jquery.nestable.js',
                      baseurl+'/static/bower_components/nestable/jquery.nestable.css'],
  filestyle:      [   baseurl+'/static/bower_components/bootstrap-filestyle/src/bootstrap-filestyle.js'],
  slider:         [   baseurl+'/static/bower_components/bootstrap-slider/bootstrap-slider.js',
                      baseurl+'/static/bower_components/bootstrap-slider/bootstrap-slider.css'],
  chosen:         [   baseurl+'/static/bower_components/chosen/chosen.jquery.min.js',
                      baseurl+'/static/bower_components/bootstrap-chosen/bootstrap-chosen.css'],
  TouchSpin:      [   baseurl+'/static/bower_components/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.js',
                      baseurl+'/static/bower_components/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.css'],
  wysiwyg:        [   baseurl+'/static/bower_components/bootstrap-wysiwyg/bootstrap-wysiwyg.js',
                      baseurl+'/static/bower_components/bootstrap-wysiwyg/external/jquery.hotkeys.js'],
  dataTable:      [   baseurl+'/static/bower_components/datatables/datamedia/js/jquery.dataTables.min.js',
                      baseurl+'/static/bower_components/plugins/integration/bootstrap/3/dataTables.bootstrap.js',
                      baseurl+'/static/bower_components/plugins/integration/bootstrap/3/dataTables.bootstrap.css'],
  vectorMap:      [   baseurl+'/static/bower_components/bower-jvectormap/jquery-jvectormap-1.2.2.min.js',
                      baseurl+'/static/bower_components/bower-jvectormap/jquery-jvectormap-world-mill-en.js',
                      baseurl+'/static/bower_components/bower-jvectormap/jquery-jvectormap-us-aea-en.js',
                      baseurl+'/static/bower_components/bower-jvectormap/jquery-jvectormap-1.2.2.css'],
  footable:       [   baseurl+'/static/bower_components/footable/dist/footable.all.min.js',
                      baseurl+'/static/bower_components/footable/css/footable.core.css'],
  fullcalendar:   [   baseurl+'/static/bower_components/moment/moment.js',
                      baseurl+'/static/bower_components/fullcalendar/dist/fullcalendar.min.js',
                      baseurl+'/static/bower_components/fullcalendar/dist/fullcalendar.css',
                      baseurl+'/static/bower_components/fullcalendar/dist/fullcalendar.theme.css'],
  daterangepicker:[   baseurl+'/static/bower_components/moment/moment.js',
                      baseurl+'/static/bower_components/bootstrap-daterangepicker/daterangepicker.js',
                      baseurl+'/static/bower_components/bootstrap-daterangepicker/daterangepicker-bs3.css'],
  tagsinput:      [   baseurl+'/static/bower_components/bootstrap-tagsinput/dist/bootstrap-tagsinput.js',
                      baseurl+'/static/bower_components/bootstrap-tagsinput/dist/bootstrap-tagsinput.css']

};
