# Boundless Treasures Architecture Diagram

Based on the core workflow described in Section 2.2 and detailed in Section 4.2 of the Business Plan.

```mermaid
graph TD
    %% Define Styles
    classDef input fill:#f9f,stroke:#333,stroke-width:2px;
    classDef core fill:#bbf,stroke:#333,stroke-width:2px,color:black,font-weight:bold;
    classDef app fill:#dfd,stroke:#333,stroke-width:2px,color:black;
    classDef physical fill:#fdd,stroke:#333,stroke-width:2px,color:black;
    classDef user fill:#fff,stroke:#333,stroke-width:4px,stroke-dasharray: 5 5;

    subgraph Input_Layer [Input Layer: Data Acquisition]
        A1[User / Museum Admin]:::user
        A2[Photos / 6-View Images]:::input
        A3[Unstructured Text Prompts]:::input
        A1 -->|Uploads| A2
        A1 -->|Inputs| A3
    end

    subgraph Core_Layer [The Generator: AI Asset Factory]
        direction TB
        B1(Tripo AI v3.0 Core):::core
        B2[Auto-Retopology<br/>(Web Optimization)]:::core
        B3[Stable Diffusion<br/>(Texture Repair)]:::core
        B4[Auto-Rigging<br/>(Animation Binding)]:::core
        
        A2 & A3 -->|API Call| B1
        B1 --> B2
        B2 --> B3
        B3 --> B4
        B4 -->|Output| B5([High-Fidelity 3D Asset <br/>GLB / FBX]):::core
    end

    subgraph Application_Layer [Digital Experience Layer]
        direction TB
        C1{{The Voyager<br/>First-Person Roaming}}:::app
        C2{{The Curator<br/>AR Virtual Pavilion}}:::app
        
        B5 -->|Runtime Load| C1
        B5 -->|WebXR Deployment| C2
        
        C1_F1[Unity WebGL / WeChat Mini-Program]
        C1_F2[FPS Roaming & Interaction]
        C1 --> C1_F1
        C1 --> C1_F2
        
        C2_F1[Real-World Overlay]
        C2_F2[Smart Lighting Estimation]
        C2 --> C2_F1
        C2 --> C2_F2
    end

    subgraph Physical_Layer [The Fab-Engine: Monetization End-Game]
        direction TB
        D1(Voxel-based Segmentation):::physical
        D2[Interlocking Curve Generation<br/>(12/50/100 Pieces)]:::physical
        D3[Tolerance Compensation<br/>(Smart Sinking)]:::physical
        D4[3D Printing & Packaging]:::physical
        
        C1 -->|One-Click Order| D1
        C2 -->|One-Click Order| D1
        D1 --> D2
        D2 --> D3
        D3 --> D4
        D4 -->|Delivery| E1[Physical Cultural Product]:::physical
    end

    %% Key Workflow Connections
    linkStyle default stroke-width:2px,fill:none,stroke:#333;
```

## System Modules Breakdown

### 1. Input Layer
- **Source**: Museum administrators or individual users.
- **Data**: Multi-angle photos of artifacts or descriptive text prompts.

### 2. Core Processing (The Generator)
- **Engine**: Tripo AI v3.0.
- **Pipeline**: 
    - **Generation**: Converts 2D input to 3D geometry.
    - **Optimization**: Retopologizes meshes for web performance.
    - **Enhancement**: Repairs textures and auto-rigs for animation.

### 3. Application Layer
- **The Voyager**: Unity-based virtual museum allowing FPS roaming and runtime asset loading.
- **The Curator**: WebXR-based AR experience for placing artifacts in real-world environments.

### 4. Physical Layer (The Fab-Engine)
- **Transformation**: Converts digital meshes into printable puzzle pieces.
- **Algorithm**: Uses voxel segmentation and tolerance compensation algorithms to ensure interlocking fit without glue.
