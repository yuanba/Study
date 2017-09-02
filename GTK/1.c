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

      box = xpm_label_box("1.pdf" , "folder");
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
