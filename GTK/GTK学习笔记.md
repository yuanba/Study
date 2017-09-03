### GTK开始之前

1. 什么是GTK

   GTK是用C编写的应用程序接口，用来创造模拟的GUI界面，在Linux机器上运行良好，并且是GNOME的编写语言

   已经和多个程序设计语言进行绑定，比如Python(2),C,C++

   GTK目前的版本是3.0,2.0都可以

2. 我用C而不是Python写GTK的原因

   Pythn目前的和GTK的接口是pygtk模块，该模块只存在Python2的接口，作为一个Python3的死忠粉，我头一次拒绝了Python

3. 下载方式

   Ubuntu机器下载GTK2 & GTK3

   ```bash
   sudo apt-get install gnome-devel gnome-devel-docs    # 下载GTK2和GTK3
   ```

### Begin

1. 下面的程序默认创造200*200的窗口，详细注释见下图

   ```c
   // 1.c
   #include <gtk/gtk.h>    //必要的头文件

   int main(int argc , char* argv[])
   {
       GtkWidget *window;
       gtk_init(&argc , &argv);   //初始化gtk标准参数
       window = gtk_window_new(GTK_WINDOW_TOPLEVEL);   //创造window组件，GTK_WINDOW_TOPLEVEL指示我们使用操作系统的窗口管理器(有叉号和放大缩小的那个)来修饰防止窗口，没有子构件的窗口默认大小是200*200
       gtk_widget_show(window);   //gtk部件展示,设置完所有的构件属性
       gtk_main();    //事件阻塞等待用户的事件启动,GTK是一个事件驱动包，会一直等待然后根据用户的输入将控制权传递到我们对应的函数中去
       return 0;
   }
   ```

   ```bash
   gcc 1.c `pkg-config --cflags --libs gtk+-2.0`    # 3.0也可以，但是2,3之间有些函数不匹配，本文章笔记针对2.0版本,笔者注这里的``是Linux的命令替换
   ```

2. Hello World

   1. 事件机制

      用作我们的`g_signal_connect / g_signal_connect的name参数`

      * button_press_event
      * button_release_event
      * event
      * destroy_event
      * ...

   2. 代码

      ```c
      #include <gtk/gtk.h>

      void destroy(GtkWidget* widget , gpointer data)
      {
          gtk_main_quit();    //退出图形用户界面
      }

      gint delete_event(GtkWidget* widget , GdkEvent* event,gpointer data)
      {
          g_print("delete event occurred\n");
          return TRUE;    //正常回复到gtk_main中去等待(中断信号的发出)，返回False表示该信号要继续被传播，比如这里是继续传播到destroy中做关闭处理
      }

      //按钮被点击的回调函数
      void hello(GtkWidget* widget,gpointer data)
      {
          g_print("Hello World\n");
      }

      int main(int argc , char* argv[])
      {
          //下面两个是基础构件
          GtkWidget *window;
          GtkWidget *button;
          gtk_init(&argc , &argv);   //初始化gtk
          window = gtk_window_new(GTK_WINDOW_TOPLEVEL);   //创造window组件

          /*
             绑定delete_event信号(关闭),收到信号后调用回调函数，回调函数的参数是NULL
             设置信号的函数原型 : 
               gulong g_signal_connect(gpoint *object,const gchar* name,GCallback function,gpointer function_data)
               第一个参数是发出信号的构件，第二个参数是要发送的信号，第三个是信号捕捉的时候的调用函数，第四个参数是函数的参数
               对于第三个参数的函数的基本原型如下 :
                  void callback_func(GtkWidget* widget,GdkEvent* event , gpointer callback_data);
                  第一个参数是构件的指针，第二个参数是数据指针，下面是接收NULL就是没有参数,event参数代表我们的时间的类型
               gulong g_signal_connect_swapped(gpoint* object , const char* name , GCallback func,gpointer* slot_object)
               这个信号函数和上面的唯一区别在于，调用的函数是无数据指针的，不常用

               G_OBJECT / G_CALLBACK 是宏，做关于GTK的类型转换
           */
          g_signal_connect(G_OBJECT(window) , "delete_event" , G_CALLBACK(delete_event) , NULL);

          g_signal_connect(G_OBJECT(window) , "destroy" , G_CALLBACK(destroy),NULL);
          
          //设置边框为10个像素
          gtk_container_set_border_width(GTK_CONTAINER(window) , 10);
          //创建一个按钮，上面的标签文本是hello world
          button = gtk_button_new_with_label("Hell World");
          //设置按钮的额点击事件，注意这里的clicked信号
          g_signal_connect(G_OBJECT(button) , "clicked" , G_CALLBACK(hello) , NULL);
          //再次添加我们的这个按钮的事件，当我们按下按钮的时候按照定义的顺序我们首先调用hello然后调用下面的函数，一个按钮可以设置很多的回调函数，他们按照顺序执行，这里的gtk_widget_destroy函数是系统默认的用来退出我们的程序(删除控件)，因为系统默认的函数没有数据参数所以我们使用*_swapped的连接方式连接信号
          g_signal_connect_swapped(G_OBJECT(button) , "clicked" , G_CALLBACK(gtk_widget_destroy),G_OBJECT(window));

          //装载函数，将我们的button装在到我们的window中
          gtk_container_add(GTK_CONTAINER(window) , button);
          gtk_widget_show(button);
          gtk_widget_show(window);   //gtk部件展示,调用显示，不调用不显示
          gtk_main();
          return 0;
      }
      ```

### 数据类型

1. `gint`,`gchar`等这些类型是我们的GLib系统中的一部分，表示了数字
2. GTK是面向对象的，一个空间就是一个对象

### 信号处理

1. 函数原型

   ```c
   //gulong是我们的回调函数的这个信号捕获机制的代号，目的在于我们之后的操作
   gulong g_signal_connect( gpointer object,
   						const gchar *name,
   						GCallback func,
   						gpointer func_data );
   //我们之前说了，一个控件可以存在多个回到函数并且依次执行,下面的函数可以将根据我们的gulong标记删除在之后删除我们的回调函数
   void g_signal_handler_disconnect( gpointer object,
       							  gulong   id );
   //和上面的实现机制不同，我们这个函数可以实现暂时的回调函数的连接断开
   void g_signal_handler_block( gpointer object,
   gulong   id );
   ```

2. 加强Hello World

   ```c
   #include <gtk/gtk.h>
   /* 我们新改进的回调函数。传递到该函数的数据将打印到标准输出(stdout)。*/
   void callback( GtkWidget *widget,gpointer   data )
   {
       g_print ("Hello again ­ %s was pressed\n", (gchar *) data);
   }
   /* 另一个回调函数 */
   gint delete_event( GtkWidget *widget,GdkEvent  *event,gpointer   data )
   {
       gtk_main_quit ();
       return FALSE;    //发送信号直接关闭
   }

   int main( int   argc,char *argv[] )
   {
     /* GtkWidget 是构件的存储类型 */
     GtkWidget *window;
     GtkWidget *button;
     GtkWidget *box1;
     /* 这个函数在所有的 GTK 程序都要调用。参数由命令行中解析出来并且送到该程序中。*/
     gtk_init (&argc, &argv);
     /* 创建一个新窗口 */
     window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
     /* 这是一个新的调用,设置窗口标题为"Hello Buttons!" */
     gtk_window_set_title (GTK_WINDOW (window), "Hello Buttons!");
     /* 在这里我们为 delete_event 设置了一个处理函数来立即退出 GTK。*/
     g_signal_connect (G_OBJECT (window), "delete_event",G_CALLBACK (delete_event), NULL);
     /* 设置窗口边框的宽度。 */
     gtk_container_set_border_width (GTK_CONTAINER (window), 10);
     /* 我们创建了一个组装盒。详情参见“组装”章节。
     * 我们看不见组装盒,它仅被作为排列构件的工具。*/
     box1 = gtk_hbox_new (FALSE, 0);
     /* 把组装盒放入主窗口中。*/
     gtk_container_add (GTK_CONTAINER (window), box1);
     /* 创建一个标签为 "Button 1" 的新按钮。*/
     button = gtk_button_new_with_label ("Button 1");
     /* 当按钮被按下时,我们调用 "callback" 函数,并将一个指向 "button 1" 的
     * 指针作为它的参数。*/
     g_signal_connect (G_OBJECT (button), "clicked",G_CALLBACK (callback), "button 1"); 
     /* 代替 gtk_container_add,我们把按钮放入不可见的组装盒,该组合盒已经组
     * 装进窗口中了。*/
     gtk_container_add(GTK_CONTAINER(box1) , button);
     gtk_widget_show(window);
     gtk_widget_show(button);
     gtk_widget_show(box1);　　　//box1不show其中的东西和他很身都看不见
     gtk_main();
   }
   ```

### 组装构件

1. 引入组装盒

   我们引入看不见的组装盒实现将我们的构建嵌套的放入我们的界面中，组装盒可以嵌套

   * hbox : 横向盒，纵向分割，控件高度一样
   * vbox : 纵向盒，横向分割，控件宽度一样

2. 创建

   ```c
   gtk_hbox_new();
   gtk_vbox_new();
   ```

3. 组装方式

   ```c
   //调整控件在box中的对齐方式
   gtk_box_pack_start();   // 上->下，左->右，组装
   gtk_box_pack_end();
   ```

4. 细节

   ```c
   void gtk_box_pack_start( GtkBox    *box,   //盒子
   						 GtkWidget *child,　　//要装载的对象
   						 gboolean   expand,　　　//TRUE默认全部填充盒子，否则不并且可以设定左右上下对齐
   						 gboolean   fill,    //多余空间是怎么分配，TRUE是对象本身，False则是围绕，只有expand为TRUE才生效
   						 guint      padding );

   GtkWidget *gtk_hbox_new ( gboolean homogeneous,　　　　//内部对象大小等大，忽略上面的expand参数
   						　 gint     spacing );     //对象
   ```

5. 表组装

   ```c
   GtkWidget *gtk_table_new( guint    rows,    //表行数
   						  guint    columns,　　　　//表列数
   						  gboolean homogeneous );　　　// TRUE : 每个格子的大小遵从我们的最大构建，否则选取同行最高同列最宽
   ```

   ```c
   void gtk_table_attach( GtkTable         *table,   //表
   					   GtkWidget        *child,   //放入的构件
   					   guint            left_attach,　　//左边界的位置，0代表表的左边第一列
   					   guint            right_attach,   //右边界的位置
   					   guint            top_attach,
   					   guint            bottom_attach,
   					   GtkAttachOptions xoptions,　　　//xoptions,yoptions的选项可以是GTK_FILL(扩展充满)/GTK_SHRINK(缩小构件同格子)/GTK_EXPAND(表扩展所有的窗口空间)
   					   GtkAttachOptions yoptions,
   					   guint            xpadding,
   					   guint            ypadding );

   //制定的行和列之间留白
   void gtk_table_set_row_spacing( GtkTable *table,
   							　　 guint     row,
   guint     spacing );

   void gtk_table_set_col_spacing( GtkTable *table,
   guint     row,
   guint     spacing );
   ```

6. 示例

   ```c
   #include <gtk/gtk.h>
   /* 我们的回调。
   * 传到这个函数的数据被打印到标准输出 */
   void callback( GtkWidget *widget,gpointer   data )
   {
   	g_print("Hello again ­ %s was pressed\n", (char *) data);    //打印到标准输出
   }
   /* 这个回调退出程序 */
   gint delete_event( GtkWidget *widget,GdkEvent  *event,gpointer   data )
   {
   	gtk_main_quit ();
   	return FALSE;
   }

   int main( int   argc,char *argv[] )
   {
   	GtkWidget *window;
   	GtkWidget *button;
   	GtkWidget *table;
   	gtk_init (&argc, &argv);
   	/* 创建一个新窗口 */
   	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
   	/* 设置窗口标题 */
   	gtk_window_set_title (GTK_WINDOW (window), "Table");
   	/* 为 delete_event 设置一个立即退出 GTK 的处理函数。 */
   	g_signal_connect (G_OBJECT (window), "delete_event",G_CALLBACK (delete_event), NULL);
   	/* 设置窗口的边框宽度。 */
   	gtk_container_set_border_width (GTK_CONTAINER (window), 20);
   	/* 创建一个 2x2 的表 */
   	table = gtk_table_new (2, 2, TRUE);
   	/* 将表放进主窗口 */
   	gtk_container_add (GTK_CONTAINER (window), table);
   	/* 创建第一个按钮 */
     	button = gtk_button_new_with_label ("button 1");
   	/* 当这个按钮被点击时,我们调用 "callback" 函数,并将一个
   	* 指向"button 1"的指针作为它的参数 */
   	g_signal_connect (G_OBJECT (button), "clicked",G_CALLBACK (callback), "button 1");
   	/* 将 button 1 插入表的左上象限(quadrant) */
   	gtk_table_attach_defaults (GTK_TABLE (table), button, 0, 1, 0, 1);
       gtk_widget_show(table);
       gtk_widget_show(window);
       gtk_widget_show(button);
       gtk_main();
   }
   ```

### 构件概述

构件创建的思路

* `gtk_*_new()`创建构件
* 连接信号和回调函数
* 设定构件属性
* 将构架加入到我们的具体的box中
* `gtk_widget_show`显示构件 / `gtk_widget_hide隐藏构件`，我们所有需要展示的构件都需要show出来，最后show我们的window

### 类型转换

1. GTK使用宏进行我们的类型转换

2. 常用的宏

   * G_OBJECT(object)
   * GTK_WIDGET(widget)
   * GTK_OBJECT(object)
   * GTK_SIGNAL_FUNC (function)
   * GTK_CONTAINER (container)
   * GTK_WINDOW (window)
   * GTK_BOX (box)

3. 细节

   `GtkWidget`是`Gobject`的基本类派生，我们可以对前者使用`G_OBJECT`宏转化

   ```c
   //例如
   g_signal_connect( G_OBJECT (button), "clicked",
   				　G_CALLBACK (callback_function), callback_data);
   ```

### 按钮构件

#### 一般按钮

```c
//创建标签按钮
gtk_button_new_with_label();
gtk_button_new_with_mnemonic();
//空白按钮
gtk_button_new();
```

```c
    #include <stdlib.h>
    #include <gtk/gtk.h>
    /* 创建一个新的横向盒,它包含一个图像和一个标签,并返回这个盒。*/
    GtkWidget *xpm_label_box( gchar *xpm_filename,gchar *label_text )
    {
        GtkWidget *box;
        GtkWidget *label;
        GtkWidget *image;
        /* 为图像和标签创建盒 */
        box = gtk_hbox_new (FALSE, 0);
        gtk_container_set_border_width (GTK_CONTAINER (box), 2);
        /* 创建一个图像,利用路径读取 */
        image = gtk_image_new_from_file (xpm_filename);
        /* 为按钮创建一个标签 */
        label = gtk_label_new (label_text);
        /* 把图像和标签组装到盒子里 */
        gtk_box_pack_start (GTK_BOX (box), image, FALSE, FALSE, 3);
        gtk_box_pack_start (GTK_BOX (box), label, FALSE, FALSE, 3);
        gtk_widget_show (image);
        gtk_widget_show (label);
        return box;    //将box内部的东西填充完之后就可以实现将box返回(指针)给其他的box或者window
    }

    void callback(GtkWidget* widget , gpointer data)
    {
      g_print("Print something to the terminal.");	
    }

    int main(int argc , char* argv[])
    {
      GtkWidget* window;
      GtkWidget* box;
      GtkWidget* button;

      gtk_init(&argc,&argv);
      window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
      gtk_window_set_title(GTK_WINDOW(window) , "Buttons Click!");

      box = xpm_label_box("绝对路径" , "folder");
      button = gtk_button_new();
      gtk_container_add(GTK_CONTAINER(button) , box);
      gtk_container_add(GTK_CONTAINER(window) , button);
      //这样写是一个好习惯
      g_signal_connect(G_OBJECT(window), "destroy" , G_CALLBACK(gtk_main_quit) ,NULL);
      gtk_widget_show(box);
      gtk_widget_show(button);
      gtk_widget_show(window);
      gtk_main();
    }
```

信号

* clicked : 点击并释放
* enter : 鼠标移入显示
* leave : 鼠标移出显示

#### 开关按钮(toggle button)

可以引用在比如**记住密码选项上**

只有开启和关闭两个状态

1. 创建

   ```c
   GtkWidget *gtk_toggle_button_new( void );
   GtkWidget *gtk_toggle_button_new_with_label( const gchar *label );
   GtkWidget *gtk_toggle_button_new_with_mnemonic( const gchar *label );
   ```

2. 检测

   我们通过读取开关构件的`active`域来检测开关的工作状态

   当我们的开关构件打开的时候会发送`toggled`信号和`clicked`信号，我们可以设置捕获`toggled`的函来处理这个信号

   `eg:`

   ```c
   //获取开关构件状态
   void toggle_button_callback (GtkWidget *widget, gpointer data)
   {
     if (gtk_toggle_button_get_active (GTK_TOGGLE_BUTTON (widget)))     //使用宏庄花成开关构件进而判断开关是否打开，函数返回值是开关挡墙的工作状态
     {
   	/* 如果运行到这里,开关按钮是按下的 */
     } 
     else 
     {
   	/* 如果运行到这里,开关按钮是弹起的 */
     }
   }

   //设置开关构件状态
   void gtk_toggle_button_set_active( GtkToggleButton *toggle_button,gboolean is_active );   //该开始默认是FALSE不开启
   ```

#### 复选按钮

1. 构件特点

   用在应用程序中的切换我们的个选项开关应用中

   * 左边是小方框等，右边是提示文字
   * 可以多选

2. 创建

   ```c
   GtkWidget *gtk_check_button_new( void );
   GtkWidget *gtk_check_button_new_with_label ( const gchar *label );
   GtkWidget *gtk_check_button_new_with_mnemonic ( const gchar *label );

   gboolean gtk_check_button_get_active(GTK_CHECK_BUTTON(widget));
   void gtk_check_button_set_active(GtkToggleButton *toggle_button,gboolean is_active );
   ```

#### 单选按钮

1. 特点

   一个时间点下，只能有一个选项处于选中状态

2. 创建

   ```c
   GtkWidget *gtk_radio_button_new( GSList *group );
   GtkWidget *gtk_radio_button_new_from_widget( GtkRadioButton *group );
   GtkWidget *gtk_radio_button_new_with_label( GSList *group,const gchar  *label );	
   //我们注意到了调用函数的参数是一个组，这里我们需要解释一下
   //单选按钮是在一个组里面工作的，一个组里有很多的单选按钮，一次只能在组里选一个
   //第一添加单选按钮的时候我们的参数是NULL
   //之后的添加的单选按钮实在组中添加的
   GSList *gtk_radio_button_get_group( GtkRadioButton *radio_button );　　  //group组是GSList的指针
   //第一次添加单选按钮之后使用上面的函数获取组，将组作为下一个参数床底给下一个单选按钮，连锁执行

   //或者使用下面的函数方法
   button2 = gtk_radio_button_new_with_label_from_widget(GTK_RADIO_BUTTON (button1), "button2");
   ```

3. 组里的默认选项设定

   ```c
   void gtk_toggle_button_set_active( GtkToggleButton *toggle_button,gboolean state );    //设定第几个单选按钮被默认激活
   ```

### 调整对象

1. 描述

   GTK 用一个调整对象(Adjustment object)解决了这个问题。**调整对象不是构件**,但是为构件提供了一种以抽象、灵活的方法来传递调整值信息。调整对象最明显的用处就是为范围构件(比如滚动条和比例构件)储存配置参数和值。然而,因为调整对象是从 Object 派生的,在其正常的数据结构之外,它还具有一些特殊的功能。最重要的是,它们能够引发信号,就像构件一样,这些信号不仅能够让程序对用户在可调整构件上的输入进行响应,还能在可调整构件之间透明地传播调整值。

2. 适用场合

   * 滚动条
   * 视角
   * 滚动窗口

3. 创建

   * 使用调整对象的构件会自动创建

   * 手动创建

     ```c
     GtkObject *gtk_adjustment_new( gdouble value,    //调整对象的初始值
     							   gdouble lower,    //调整对象最低取值
     							   gdouble upper,    //分栏构件参数
     							   gdouble step_increment,    //改变值的步长
     							   gdouble page_increment,
     							   gdouble page_size );
     ```

4. 使用调整对象

   1. 特点

      * 所有使用调整对象的构件**都可以使用自己的调整对象**,或者使用你创建的调整对象,但是最好让这一类构件都使用它们自己的调整对象。
      * 前面说过,和其它构件一样,调整对象是 Object 的子类,因而,它也能够引发信号。这也是为什么当滚动条和其它可调整构件共享调整对象时它们能够自动更新的原因。

   2. 使用

      当构件重新配置了它的调整对象的 upper 或 lower 参数时(比如,用户向文本构件添加了更多的文本时),发生了什么?在这种情况下,它会引发一个 changed 信号:

      ```c
      void (* changed) (GtkAdjustment *adjustment);
      ```

      范围构件一般为这个信号设置回调函数,构件会改变它们的外观以反映变化。例如,滚动条上的滑块会根据它的调整对象的 lower 和 upper 参数之间的差值的变化而伸长或缩短

5. 范围构件

6. 滚动条构件

   1. 创建

      ```c
      //参数是NULL的时候默认创建一个调整对象
      GtkWidget *gtk_hscrollbar_new( GtkAdjustment *adjustment );
      GtkWidget *gtk_vscrollbar_new( GtkAdjustment *adjustment );    
      ```

   ​

   ​

   ​