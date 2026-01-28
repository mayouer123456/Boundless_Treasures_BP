# 无界遗珍 (Boundless Treasures) 系统架构图

基于商业计划书 2.2 核心流程与 4.2 产品技术细节绘制。

```mermaid
graph TD
    %% 定义样式
    classDef input fill:#f9f,stroke:#333,stroke-width:2px;
    classDef core fill:#bbf,stroke:#333,stroke-width:2px,color:black,font-weight:bold;
    classDef app fill:#dfd,stroke:#333,stroke-width:2px,color:black;
    classDef physical fill:#fdd,stroke:#333,stroke-width:2px,color:black;
    classDef user fill:#fff,stroke:#333,stroke-width:4px,stroke-dasharray: 5 5;

    subgraph Input_Layer [输入层: 数据采集 (Input Layer)]
        A1[用户 / 博物馆管理员]:::user
        A2[照片 / 六视图]:::input
        A3[非结构化文本提示词]:::input
        A1 -->|上传| A2
        A1 -->|输入| A3
    end

    subgraph Core_Layer [生成层: AI 资产工厂 (The Generator)]
        direction TB
        B1(Tripo AI v3.0 核心引擎):::core
        B2[自动拓扑<br/>(Web端优化)]:::core
        B3[Stable Diffusion<br/>(纹理修复)]:::core
        B4[自动骨骼绑定<br/>(动效适配)]:::core
        
        A2 & A3 -->|API 调用| B1
        B1 --> B2
        B2 --> B3
        B3 --> B4
        B4 -->|输出| B5([高保真 3D 资产 <br/>GLB / FBX]):::core
    end

    subgraph Application_Layer [应用层: 数字化体验 (Voyager & Curator)]
        direction TB
        C1{{漫游展厅 (The Voyager)<br/>第一人称漫游}}:::app
        C2{{AR 展馆 (The Curator)<br/>虚拟展厅}}:::app
        
        B5 -->|Runtime 动态加载| C1
        B5 -->|WebXR 部署| C2
        
        C1_F1[Unity WebGL / 微信小程序]
        C1_F2[FPS 漫游与交互]
        C1 --> C1_F1
        C1 --> C1_F2
        
        C2_F1[虚实叠加 (Real-World Overlay)]
        C2_F2[智能光照估计 (Smart Lighting)]
        C2 --> C2_F1
        C2 --> C2_F2
    end

    subgraph Physical_Layer [物理层: 实体转化引擎 (The Fab-Engine)]
        direction TB
        D1(体素化分割 Voxel Segmentation):::physical
        D2[互锁曲线生成<br/>(12/50/100 片)]:::physical
        D3[公差补偿<br/>(智能收缩计算)]:::physical
        D4[3D 打印与封装]:::physical
        
        C1 -->|一键下单| D1
        C2 -->|一键下单| D1
        D1 --> D2
        D2 --> D3
        D3 --> D4
        D4 -->|发货| E1[实体文创产品]:::physical
    end

    %% 关键工作流连接
    linkStyle default stroke-width:2px,fill:none,stroke:#333;
```

## 系统模块详解

### 1. 输入层 (Input Layer)
- **来源**：博物馆管理员或个人用户。
- **数据**：文物的多角度照片（推荐六视图）或描述性文本 Prompt。

### 2. 核心处理层 (The Generator)
- **引擎**：Tripo AI v3.0。
- **管线**：
    - **生成**：将 2D 输入转化为 3D 几何体。
    - **优化**：自动拓扑 (Auto-Retopology) 以适应 Web 端性能。
    - **增强**：纹理修复 (Texture Repair) 与自动骨骼绑定 (Auto-Rigging)。

### 3. 应用层 (Application Layer)
- **The Voyager (漫游展厅)**：基于 Unity 的虚拟博物馆，支持 FPS 漫游与 Runtime 资产热加载。
- **The Curator (AR 展馆)**：基于 WebXR 的 AR 体验，将文物无缝融入真实环境。

### 4. 物理层 (The Fab-Engine)
- **转化**：将数字模型转化为可打印的拼图组件。
- **算法**：利用体素分割与公差补偿算法，确保无需胶水即可实现互锁 (Interlocking) 拼装。
