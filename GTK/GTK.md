* window

  * gtk_window_set_title(window , const gchar* name);

  * gtk_window_set_default_size(window,int width,int height);

  * gtk_window_set_position(window , GtkWindowPosition position);

  * gtk_window_new(GTK_WINDOW_POPUP)窗口无边框

    后一个参数是几个宏

    * GTK_WIN_POS_NONE : 不固定
    * GTK_WIN_POS_CENTER : 居中
    * GTK_WIN_POS_MOUNSE

  * 一个窗口一次只能容纳一个控件，再添加会导致错误，利用加盒子的方式可以拓展这个缺陷

* 控件类型

  * 容器型
  * 非容器型

  容器方式可以实现我们的内容的分布

  ```c
  gtk_container_add(GTK_CONTAINER(window) , widget);   //一个容器一次只能加一个,盒子可以加多个
  ```

* 盒子控件    

  * gtk_hbox_new
  * gtk_vbox_new

* 显示

  * gtk_widget_show(widget)
  * gtk_widget_show_all

* 表

  * gtk_table_new(nrow , ncol , Bool)
  * gtk_table_attach(GTK_TABLE(table) , button , n , n , n ,n)

* 图像

  GtkWidget image = gtk_image_new_from_file("path")

* 标签

  gtk_label_new("文本字符串")

  标签美化

  * 文字对齐

    gtk_label_set_justify(GTK_LABEL(label) , GTK_JUSTIFY_LEFT / RIGHT / CENTER / FILL)

  * 格式化标签文本

    gtk_label_set_mark(GTK_LABEL(label) , title)用HTML的形式美化字体

  * 自动换行

    gtk_label_set_line_wrap(GTK_LABEL(label) , TRUE)TRUE设置换行

* 箭头

  gtk_arrow_button(GTK_ARROW_LEFT / UP / DOWN / RIGHT , GTK_SHADOW_NONE / GTK_SHADOW_IN / GTK_SHADOW_OUT);

* 菜单

  * GtkAccelGroup* accel_group = gtk_accel_group_new()

    gtk_window_add_accel_group(GTK_WINDOW(window) , accel_group)

  * 先定义GtkItemFactoryEntry meanu_item,多行字符串数组

    GtkItemFactory* item_factory = gtk_item_factory_new(GTK_TYPE_MENU_BAR , "<main>" , accel_group)

    gtk_item_factory_create_items(item_factory , n , menu_items , NULL);

  * 信号

    `activate`信号表示激活

* 工具条

  * gdb_toolbar_new()创建工具条，工具条可以添加到其他的控件和容器中
  * gdb_toolbar_append_item()添加文字和按钮