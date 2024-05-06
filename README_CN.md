**LogView 项目 README**

📁 **项目结构**
```
📂 LogView
.
├── AuthView.py
├── KernelView.py
├── LICENSE
├── MongodbView.py
├── NginxErrorView.py
├── NginxView.py
├── README.md
├── README_CN.md
├── README_KR.md
├── SysLogView.py
├── 📂doc
│   ├── AuthView.md
│   ├── AuthView_CN.md
│   ├── AuthView_KR.md
│   ├── KernelView.md
│   ├── KernelView_CN.md
│   ├── KernelView_KR.md
│   ├── MongodbView.md
│   ├── MongodbView_CN.md
│   ├── MongodbView_KR.md
│   ├── NginxErrorView.md
│   ├── NginxErrorView_CN.md
│   ├── NginxErrorView_KR.md
│   ├── NginxView.md
│   ├── NginxView_CN.md
│   ├── NginxView_KR.md
│   ├── SysLogView.md
│   ├── SysLogView_CN.md
│   └── SysLogView_KR.md
├── 📂example_log
│   ├── auth.log
│   ├── kern.log
│   ├── mongod.log
│   ├── 📂nginx
│   │   ├── access.log
│   │   └── error.log
│   └── syslog
├── generate_logs.py
├── test_output.py
└── 📂video
    └── demo.webm

5 directories, 37 files
```
该项目处理和分析各种日志类型，帮助理解系统状态并解决问题。每个模块提供对特定类型日志的详细信息，并帮助用户诊断和解决问题。

**演示视频**

![Demonstration Video](./docs/demo.gif)

**doc**

快速查看 doc 文件夹中的文档，了解每个文件的作用！

**提示：如果您要使用这些工具，请将路径修改为实际路径，因为当前路径是示例日志路径。**