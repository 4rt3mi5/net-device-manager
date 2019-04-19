var _table_info = {
    "emptyTable": "没有数据",
    "info": "显示第 _START_ 至 _END_ 项结果；总共 _TOTAL_ 项",
    "paginate": {
        "previous": "上一页",
        "next": "下一页"
    },
    "lengthMenu": '每页 <select class="form-control input-sm">'+
        '<option value="10">10</option>'+
        '<option value="20">20</option>'+
        '<option value="30">30</option>'+
        '<option value="40">40</option>'+
        '<option value="50">50</option>'+
        '<option value="-1">All</option>'+
        '</select> 项',
    "search": "搜索： _INPUT_ ",
    "infoFiltered": "(总共 _MAX_ 项)"
}

// index.html begin

// 添加节点
function addNode(text, x , y, popup_text, type, status){
    var node = new JTopo.Node();
    node.setImage('/static/img/' + type + '.png', true);
    node.fontColor = '0,0,0';
    node.setLocation(x, y);
    node.text = text;
    scene.add(node);

    node.mouseover(function(){
        this.alarm = popup_text;
        this.alarmColor = '0,255,0';
        this.alarmAlpha = 0.9;
    });

    node.mouseout(function(){
        this.alarm = null;
    });
    if (status == 'False' || status == 'None')
    {
        changeNodeAbnormal(node,popup_text);
    };
    return node;
}

// 更改节点为标准状态
function changeNodeNormal(node,text){
    node = eval(node)
    node.alarm = null;
    node.alarmColor = '0,255,0';
    node.alarmAlpha = 0.9;
    node.mouseover(function(){
        this.alarm = text;
        this.alarmColor = '0,255,0';
        this.alarmAlpha = 0.9;
    });

    node.mouseout(function(){
        this.alarm = null;
    });
    return node;
}

// 更改节点为警告状态
function changeNodeAbnormal(node,text){
    node = eval(node)
    node.alarm = text;
    node.alarmColor = '255,0,0';
    node.alarmAlpha = 0.9;
    node.mouseover(function(){
        this.alarm = text;
        this.alarmColor = '255,0,0';
        this.alarmAlpha = 0.9;
    });

    node.mouseout(function(){
        this.alarm = text;
        this.alarmColor = '255,0,0';
        this.alarmAlpha = 0.9;
    });
    return node;
}

// 添加连接线条
function addLink(nodeA, nodeZ){
    var link = new JTopo.Link(nodeA, nodeZ);
    link.strokeColor = '144,238,144';
    link.lineWidth = 2;
    scene.add(link);
    return link;
}

// 添加连接虚线
function addLightLink(nodeA, nodeZ){
    var link = new JTopo.Link(nodeA, nodeZ);
    link.strokeColor = '30,144,255';
    link.lineWidth = 2;
    link.dashedPattern = 5;
    scene.add(link);
    return link;
}

// index.html end

// device list.html begin

//改变设备列表页面
function changeDeviceListUI() {
    var add_device = '<a href="/admin/device/device/add/" class="btn btn-primary btn-sm float-r" style="margin-bottom:7px"> 添加设备</a>';
    var btn_ex_im = '<a href="#" data-toggle="modal"  data-target="#UploadDevice" class="btn btn-default btn-sm float-r" style="margin-right:3px"> 导入</a><a href="/api/device/export" class="btn btn-default btn-sm float-r"> 导出</a>';
    $('#dataTables-device').DataTable({
        responsive: true,
        bAutoWidth: true,
        "dom": "<'row'<'#add_device.col-lg-12'><'col-md-6'l><'col-md-6'<'#btn_ex_im.col-lg-3 plus-times'>f>r>" +
            "t" +
            "<'row'<'col-md-5 sm-center'i><'col-md-7 text-right sm-center'p>>",
        "language": _table_info
    });
    $("#add_device").append(add_device);
    $("#btn_ex_im").append(btn_ex_im);
};

// device list.html end

// device group list.html begin

//改变设备组列表页面
function changeDeviceGroupListUI() {
    var add_group = '<a href="/admin/device/devicegroup/add/" class="btn btn-primary btn-sm float-r" style="margin-bottom:7px"> 添加设备组</a>';
    $('#dataTables-group').DataTable({
        responsive: true,
        bAutoWidth: true,
        "dom": "<'row'<'#add_group.col-lg-12'><'col-md-6'l><'col-md-6'f>r>" +
            "t" +
            "<'row'<'col-md-5 sm-center'i><'col-md-7 text-right sm-center'p>>",
        "language": _table_info
    });
    $("#add_group").append(add_group);
};

// device group list.html end

// user login_log.html begin

// 改变登录日志列表页面
function changeLoginlogListUI() {
    var dom_ele = '<form action="" method="get"><div class="form-group" ><div class="input-daterange input-group"><span class="input-group-addon"><i class="fa fa-calendar"></i></span><input type="date" class="input-sm form-control" style="width: 150px;" name="date_from" value="2018-02-04"><span class="input-group-addon">to</span><input type="date" class="input-sm form-control" style="width: 150px;" name="date_to" value="2018-02-11"></div><div class="input-group"><select class="input-sm form-control" style="width:100px;margin:0px 5px" name="username"><option></option>{% for user in user_object %}<option>{{ user.username }}</option>{% endfor %}</select></div><div class="input-group"><input type="text" class="form-control input-sm" style="width:150px;" name="keyword"></div><div class="input-group"><input type="submit" class="btn btn-sm btn-primary" value="搜索"></div></div></form>';
    $('#dataTables-loginlog').DataTable({
        responsive: true,
        bAutoWidth: true,
        "dom": "<'row'<'col-md-4'l><'col-md-8'<'#newDOM'>>r>" +
            "t" +
            "<'row'<'col-md-5 sm-center'i><'col-md-7 text-right sm-center'p>>",
        "language": _table_info
    });
    $("#newDOM").append(dom_ele);
}

// user login_log.html end

// ap ap_search.html begin

// 搜索MAC地址
function searchClientAddress() {
    var mac_address = $("input[name='search']").val()
    if (mac_address.split(':').length != 6) {
        alert('请输入正确的MAC地址')
        return
    }
    alert('正在查找，请稍后...')
    $.ajax({
        type: "get",
        url: "/api/ap/search-client",
        data: {mac:mac_address},
        dataType: "json",
        success: function (response) {
            console.log(response)
            if ('error' in response){
                alert(response.error)
                return
            }
            var line = '<td class="text-center">' + response['Client MAC Address'] + '</td>' + 
            '<td class="text-center">' + response['IP Address'].replace(/:/g,'.') + '</td>' + 
            '<td class="text-center">' + response['IPv6 Address'] + '</td>' + 
            '<td class="text-center">' + response['AP Name'] + '</td>' + 
            '<td class="text-center">' + response['Protocol'] + '</td>' + 
            '<td class="text-center">' + response['Client Username'] + '</td>' + 
            '<td class="text-center">' + response['Connected For'] + '</td>' + 
            '<td class="text-center">' + response['Channel'] + '</td>' + 
            '<td class="text-center">' + response['Gateway Address'] + '</td>' + 
            '<td class="text-center">' + response['DNS server IP'].replace(/:/g,'.') + '</td>'
            $('tbody').append('<tr>' + line + '</tr>')
        }
    });
}

// ap ap_search.html end

// node list.html begin
//改变节点列表页面
function changeNodelistUI() {
    var add_node = '<a href="/admin/node/node/add/" class="btn btn-primary btn-sm float-r" style="margin-bottom:7px"> 添加节点</a>';
    $('#dataTables-node').DataTable({
        responsive: true,
        bAutoWidth: true,
        "dom": "<'row'<'#add_node.col-lg-12'><'col-md-6'l><'col-md-6'f>r>" +
            "t" +
            "<'row'<'col-md-5 sm-center'i><'col-md-7 text-right sm-center'p>>",
        "language": _table_info
    });
    $("#add_node").append(add_node);
};

// node list.html end


// node connect list.html begin
//改变节点连接列表页面
function changeNodeConnectlistUI() {
    var add_node_connect = '<a href="/admin/node/nodeconnect/add/" class="btn btn-primary btn-sm float-r" style="margin-bottom:7px"> 添加节点连接</a>';
    $('#dataTables-node-connect').DataTable({
        responsive: true,
        bAutoWidth: true,
        "dom": "<'row'<'#add_node_connect.col-lg-12'><'col-md-6'l><'col-md-6'f>r>" +
            "t" +
            "<'row'<'col-md-5 sm-center'i><'col-md-7 text-right sm-center'p>>",
        "language": _table_info
    });
    $("#add_node_connect").append(add_node_connect);
};


// node connect list.html end


// ap ap-list.html  begin

function changeAplistUI() {
    $('#dataTables-ap-list').DataTable({
        responsive: true,
        bAutoWidth: true,
        "language": _table_info
    });
}

// 获得ap 列表
function getAPlist(url) {
    $('#waitModal').modal('show')
    $.ajax({
        type: "get",
        url: url,
        data: "",
        dataType: "json",
        success: function (response) {
            if ('error' in response){
                alert(response.error);
                window.document.href='/';
            }else {
                console.log(response);
                $('#waitModal').modal('hide');
                window.location.href='/device/ap-list'
            }
        },
        error: function(data) {
            alert(JSON.stringify(data));
            window.location.href='/';
        }
    });
}


// 重启AP
function rebootAP(ap_name) {
    var status = confirm('确定要重启[' + ap_name + ']设备吗？')
    if (status == false){
        return
    }
    alert('设备正在重启，请稍后...')
    $.ajax({
        type: "get",
        url: "/api/ap/reboot",
        data: {ap_name:ap_name},
        dataType: "json",
        success: function (response) {
            if (response.msg == 'true'){
                console.log(response)
            }else{
                alert(response.msg)
            }
            window.document.href='/device/ap-list'
        }
    });
}
// ap ap-list.html end


// device device_list.html begin
// 查看配置信息

function getConfig(id, data, to_url, re_url) {
    $('#waitModal').modal('show')
    if (data == 'true'){
        var arg = 'true'
    }else{
        var arg = 'none'
    }
    $.ajax({
        type: "get",
        url: to_url + id,
        data: {update:arg},
        dataType: "json",
        success: function (response) {
            if ('error' in response){
                alert(response.error);
                window.location.href='/';
            }else {
                console.log(response);
                $('#waitModal').modal('hide');
                window.location.href=re_url + id
            }
        },
        error: function(data) {
            alert(JSON.stringify(data));
            window.location.href='/';
        }
    });
}


// device device_list.html end

// device config.html begin
function addConfig(id) {
    $('#waitModal').modal('show')
    var string = ['timeline-inverted', 'none']
    var reg1 = new RegExp("<","g")
    var reg2 = new RegExp(">","g")
    var value = string[Math.round(Math.random())];  //随机抽取一个值
    var color = ['warning','danger','info','success']
    var value_color = color[Math.round(Math.random()*(color.length-1))]; 
    var ele1 = '<li class="' + value + '">' + 
        '<div class="timeline-badge"><i class="fa fa-check"></i>' + 
        '</div>' + 
        '<div class="timeline-panel">' + 
            '<div class="timeline-heading">' + 
                '<h4 class="timeline-title">'
    var ele2 = '</h4>' + 
                '<p><small class="text-muted"><i class="fa fa-clock-o"></i> '
    var ele3 = '</small>' + 
                '</p>' + 
            '</div>' + 
            '<div class="timeline-body">' + 
                '<pre class="pre-scrollable">'
    var ele4 = '</pre>' + 
            '</div>' + 
       ' </div>' + 
    '</li>'
    $.ajax({
        type: "get",
        url: "/api/config/get-detail/" + id,
        data: "",
        dataType: "json",
        success: function (response) {
            if ('error' in response){
                console.log(response.error);
                $.ajax({
                    type: "get",
                    url: "/api/config/running/" + id,
                    data: "",
                    dataType: "json",
                    success: function (response) {
                        if ('error' in response){
                            alert(response.error);
                            window.document.href='/';
                        }else {
                            $.ajax({
                                type: "get",
                                url: "/api/config/get-detail/" + id,
                                data: "",
                                dataType: "json",
                                success: function (response) {
                                    $('#waitModal').modal('hide');
                                    var result = ele1 + response.ip + ' (' + response._config_id + ')' + 
                                    ele2 + response._config_create_time + 
                                        ele3 + response._config_config.replace(reg1, '&lt;').replace(reg2,'&gt;') + ele4
                                    console.log(result)
                                    $('.timeline').append(result)
                                    $('.timeline-badge').click(function(){
                                        $(this).addClass(value_color)
                                    })
                                }
                            });
                        }
                    },
                    error: function(data) {
                        alert(JSON.stringify(data));
                        window.location.href='/';
                    }
                });
            }else {
                console.log(response);
                $('#waitModal').modal('hide');
                var result = ele1 + response.ip + ' (' + response._config_id + ')' + 
                    ele2 + response._config_create_time + 
                    ele3 + response._config_config.replace(reg1, '&lt;').replace(reg2,'&gt;') + ele4
                console.log(result)
                $('.timeline').append(result)
                $('.timeline-badge').click(function(){
                    $(this).addClass(value_color)
                })
            }
        },
        error: function(data) {
            console.log(JSON.stringify(data));
            alert('未知错误')
            window.location.href='/';
        }
    });
}
// device config.html end


// monitor monitor.html begin

// 绑定端口
function boundPort(id) {
    var port = $('#port').find('option:selected').val()
    $.ajax({
        type: "get",
        url: "/api/monitor/bound-port/" + id,
        data: {port:port},
        dataType: "json",
        success: function (response) {
            if (response.msg == 'success'){
                $('#port option[value=\'' + port + '\']').remove()
                $('blockquote').append('<small>' + port + '</small>')
                $('#monitor_ports').append('<option value="' + port + '">' + port + '</option>')
                alert('绑定成功')
                return
            }
        },
        error: function(data){
            console.log(data)
            alert('未知错误')
            return
        }
    });
}


// 更新硬件动态推送数据
function update_hardware_line_chart_data(new_value) {
    HardwareChart.data.labels.splice(0, 1);
    HardwareChart.data.datasets.forEach(function(dataset) {
        dataset.data.splice(0, 1);
    });
    HardwareChart.data.labels.push(new_value['time']);
    HardwareChart.data.datasets[0].data.push(new_value["cpu"].toString());
    HardwareChart.data.datasets[1].data.push(new_value["memory"].toString());
    window.HardwareChart.update();
}
// 更新带宽动态推送数据
function update_bandwidth_line_chart_data(new_value) {
    BandwidthChart.data.labels.splice(0, 1);
    BandwidthChart.data.datasets.forEach(function(dataset) {
        dataset.data.splice(0, 1);
    });
    BandwidthChart.data.labels.push(new_value['time']);
    BandwidthChart.data.datasets[0].data.push(new_value["upload"].toString());
    BandwidthChart.data.datasets[1].data.push(new_value["download"].toString());
    window.BandwidthChart.update();
}
// 更新温度动态推送数据
function update_temperature_line_chart_data(new_value) {
    TemperatureChart.data.labels.splice(0, 1);
    TemperatureChart.data.datasets.forEach(function(dataset) {
        dataset.data.splice(0, 1);
    });
    TemperatureChart.data.labels.push(new_value['time']);
    TemperatureChart.data.datasets[0].data.push(new_value["current"].toString());
    TemperatureChart.data.datasets[1].data.push(new_value["upper"].toString());
    window.TemperatureChart.update();
}

//  更新显示方式节点数量
function updateDisplayDataTime(chart, to_length, type, id) {
    if (type == 'hardware'){
        var type1 = 'cpu'
        var type2 = 'memory'
    }else if(type == 'bandwidth'){
        var type1 = 'upload'
        var type2 = 'download'
    }else{
        var type1 = 'current'
        var type2 = 'upper'
    }
    if (chart.data.labels.length == to_length){
        return
    }else if (chart.data.labels.length > to_length){
        poor = chart.data.labels.length - to_length
        chart.data.labels.splice(0, poor);
        chart.data.datasets.forEach(function(dataset) {
            dataset.data.splice(0, poor);
        });
        chart.update()
        return 
    }else if (chart.data.labels.length < to_length){
        var node_length = to_length - chart.data.labels.length
        var from_time = chart.data.labels[0]
        var port = $('#monitor_ports option:selected').val()
        $.ajax({
            type: "get",
            url: "/api/monitor/get-range/" + id,
            data: {
                'node_length':node_length,
                'from_time':from_time,
                'type':type,
                'port': port,
            },
            dataType: "json",
            success: function (response) {
                // 反向排序数据
                response_data = response['search_result_data'].reverse()
                console.log(response_data[0].value)
                for (var pk in response_data) {
                    chart.data.labels.unshift(response_data[pk]['create_time'])
                    if (response_data[pk].value == '0'){
                        chart.data.datasets[0].data.unshift('0');
                        chart.data.datasets[1].data.unshift('0');
                    }else {
                        chart.data.datasets[0].data.unshift(response_data[pk]['value'][type1].toString());
                        chart.data.datasets[1].data.unshift(response_data[pk]['value'][type2].toString());
                    }
                }
                chart.update()
            }
        });
    }
}

// 获取端口数据
function getPortData(id) {
    var port = $('#monitor_ports').find('option:selected').val()
    $.ajax({
        type: "get",
        url: "/api/monitor/get-port-data/" + id,
        data: {
            'port': port,
            'labels_length':BandwidthChart.data.labels.length
        },
        dataType: "json",
        success: function (response) {
            console.log(response)
            var response_data = response['port_data']
            for (var pk in response_data){
                BandwidthChart.data.labels.splice(0, 1);
                BandwidthChart.data.datasets.forEach(function(dataset) {
                    dataset.data.splice(0, 1);
                });
                BandwidthChart.data.labels.push(response_data[pk]['create_time']);
                if (response_data[pk].value == '0'){
                    BandwidthChart.data.datasets[0].data.push('0');
                    BandwidthChart.data.datasets[1].data.push('0');
                }else {
                    BandwidthChart.data.datasets[0].data.push(response_data[pk]['value']['upload'].toString());
                    BandwidthChart.data.datasets[1].data.push(response_data[pk]['value']['download'].toString());
                }
            }
            BandwidthChart.update();
        }
    });
}

// 搜索时间
function searchTime(chart, type, id) { 
    if (type == 'hardware'){
        var type1 = 'cpu'
        var type2 = 'memory'
        var data = {
            'from_time':$('#hardware_time').val(),
            'type': 'hardware',
            'labels_length': chart.data.labels.length,
        }
        var stop = hardware_stop
    }else if(type == 'bandwidth'){
        var type1 = 'upload'
        var type2 = 'download'
        var data = {
            'from_time':$('#bandwidth_time').val(),
            'type': 'bandwidth',
            'labels_length': chart.data.labels.length,
            'port':$('#monitor_ports option:selected').val()
        }
        var stop = bandwidth_stop
    }else{
        var type1 = 'current'
        var type2 = 'upper'
        var data = {
            'from_time':$('#tempearture_time').val(),
            'type': 'temperature',
            'labels_length': chart.data.labels.length,
        }
        var stop = temperature_stop
    }
    $.ajax({
        type: "get",
        url: "/api/monitor/search-time/" + id,
        data: data,
        dataType: "json",
        success: function (response) {
            console.log(response)
            chart.data.labels.splice(0, chart.data.labels.length);
            chart.data.datasets.forEach(function(dataset) {
                dataset.data.splice(0, dataset.data.length);
            });
            var resp = response['search_result_data']
            for (var pk in resp) {
                chart.data.labels.push(resp[pk]['create_time'])
                if (resp[pk].value == '0'){
                    chart.data.datasets[0].data.push('0');
                    chart.data.datasets[1].data.push('0');
                }else {
                    console.log(resp[pk]['value'])
                    chart.data.datasets[0].data.push(resp[pk]['value'][type1].toString());
                    chart.data.datasets[1].data.push(resp[pk]['value'][type2].toString());
                }
            }
            chart.update()
        }
    });
}


// 更改监控项目的阈值
function changeTereshold(id) {
    var count = $('#count_vpt').val()
    var cpu = $('#cpu_vpt').val()
    var memory = $('#memory_vpt').val()
    var upload = $('#upload_vpt').val()
    var download = $('#download_vpt').val()
    var temp = $('#temperature_vpt').val()
    if (cpu == 0 || memory == 0 || upload == 0 || download == 0 || temp == 0 || count == 0){
        alert('不允许存在阈值为0')
        return
    }
    $.ajax({
        type: "get",
        url: "/api/monitor/tereshold/" + id,
        data: {
            count:count,
            cpu:cpu,
            memory:memory,
            upload:upload,
            download:download,
            temperature:temp
        },
        dataType: "json",
        success: function (response) {
            console.log(response)
            alert('设置成功')
            $('#settingModal').modal('hide')
        }
    });
}
// monitor monitor.html end

// users d_users.html begin

//改变设备用户列表页面
function changeDeviceUsersUI() {
    var add_user = '<a href="/config/create-users" class="btn btn-primary btn-sm float-r" style="margin-bottom:7px"> 添加用户</a>';
    $('#dataTables-users').DataTable({
        responsive: true,
        bAutoWidth: true,
        "dom": "<'row'<'#add_user.col-lg-12'><'col-md-6'l><'col-md-6'f>r>" +
            "t" +
            "<'row'<'col-md-5 sm-center'i><'col-md-7 text-right sm-center'p>>",
        "language": _table_info
    });
    $("#add_user").append(add_user);
};


// 删除用户
function deleteUser(id, username) {
    $('#waitModal').modal('show')
    $.ajax({
        type: "get",
        url: "/api/d-user/delete/" + id,
        data: {username:username},
        dataType: "json",
        success: function (response) {
            console.log(response)
            if (response.msg == 'true'){
                alert('删除用户 ' + username + ' 成功')
                $('waitModal').modal('hide')
                $('#deleteDUser').modal('hide')
                getConfig(id,'true','/api/d-user/get/','/config/show-users/')
            }
        }
    });
}


// 提交创建用户的数据
function createUser(token){
    $('#waitModal').modal('show')
    var devicesStr = new String();
    var username = $("input[name='username']").val()
    var password = $("input[name='password']").val()
    var level = $('#id_level option:selected').val()
    var service_type = $('#id_service_type option:selected').val()
    $('#select_right option').each(function(){
        devicesStr += $(this).val() + ',';
    });
    data = {
        "devices" : devicesStr,
        "username" : username,
        "password" : password,
        "level" : level,
        "service_type": service_type,
        "csrfmiddlewaretoken" : token,
    }
    $.ajax({
        type:'post',
        url:'/api/d-user/create',
        timeout: 30000,
        data: data,
        dataType: 'json',
        success: function(e) {
            if (e['failed'].length == 0)
            {
                alert('已创建成功');
            }else{
                error_string = ''
                for (var pk in e['failed']) {
                    error_string += e['failed'][pk] + '------失败\n'
                }
                alert(error_string)
            };
            location.reload()
        }
    });
}


// 更改设备用户密码
function changePassword(id, username, token){
    var password1 = $('#password1').val()
    var password2 = $('#password2').val()
    if (password1 != password2){
        alert('两次密码输入不同，请重新输入')
        $('#password1').val('')
        $('#password2').val('')
        return
    }
    $('#waitModal').modal('show')
    $.ajax({
        type: "post",
        url: "/api/d-user/change-password/" + id,
        data: {username:username,password:password1,csrfmiddlewaretoken:token},
        dataType: "json",
        success: function (response) {
            console.log(response)
            if ('error' in response){
                alert('更改失败，错误信息：' + response.error)
            }else{
                $('#waitModal').modal('hide')
                $('#changePassword').modal('hide')
                $('#password1').val('')
                $('#password2').val('')
            }
        }
    });

}
// users d_users.html end

// 添加用户
function addAlertUser(token){
    var s = $('#us').val()
    $.ajax({
        type: "post",
        url: "/api/alert-user/getall",
        data: {username:s,"csrfmiddlewaretoken" : token},
        dataType: "json",
        success: function (response) {
            if ('msg' in response){
                $('#alert_users').append('<a href=# onclick="javascript:deleteAlertUser(\'' + s + '\',this)"><small>' + s + '</small></a>')
                $('#us').val('')
                alert(response.msg)
            }
        }
    });
}

// 删除用户
function deleteAlertUser(username,th) {
    $.ajax({
        type: "get",
        url: "/api/alert-user/delete",
        data: {username:username},
        dataType: "json",
        success: function (response) {
            console.log(response)
            console.log(th)
            th.remove()
        }
    });
}


function settingCleanTime(token){
    var t = $('#ts').val()
    $.ajax({
        type: "post",
        url: "/api/monitor/set-clean-data",
        data: {time:t,"csrfmiddlewaretoken" : token},
        dataType: "json",
        success: function (response) {
            console.log(response)
            alert(response.msg)
        }
    });
}