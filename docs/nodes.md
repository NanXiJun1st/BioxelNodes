# Nodes

## Mask Methods

### ⬆️ Mask by Threshold

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_mask-by-threshold.png)

-   Generate a mask by keeping only the positions that exceed the threshold (this only works with scalar)

    ***

    Node Parameter:

    -   **Layer**, _the input scalar_
    -   **Threshold**, _the threshold value_
    -   Preview
        -   **Detail Factor**, _the fineness of the preview, the larger the factor, the coarser preview is_
    -   (Label Mask)
        -   **Layer**, _the input label_
        -   **Invert**, _invert mask_
        -   **Sample Size**, _the mask sample size_
    -   (Replacement)
        -   **Joined**, _the joined layer_

</div>

### ↕ Mask by Range

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_mask-by-range.png)

-   Generate a mask by keeping only the positions that in range (this only works with scalar)

    ***

    Node Parameter:

    -   **Layer**, _the input scalar_
    -   **Fram Min**, _the lower limit_
    -   **Fram Max**, _the upper limit_
    -   Preview
        -   **Detail Factor**, _the fineness of the preview, the larger the factor, the coarser preview is_
    -   (Label Mask)
        -   **Layer**, _the input label_
        -   **Invert**, _invert mask_
        -   **Sample Size**, _the mask sample size_
    -   (Replacement)
        -   **Joined**, _the joined layer_

</div>

### 🔤 Mask by Label

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_mask-by-label.png)

-   Generate a mask by keeping only the positions that in label (this only works with label)

    ***

    Node Parameter:

    -   **Layer**, _the input label_
    -   Preview
        -   **Detail Factor**, _the fineness of the preview, the larger the factor, the coarser preview is_
    -   (Replacement)
        -   **Joined**, _the joined layer_

</div>

## Shaders

### 🥚 Solid Shader

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_solid-shader.png)

-   Assign a opaque shader based on a preview mesh with no inclusions visible. Fastest rendering speed. Does not support cross-section and color ramp.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
        -   Base
        -   **Color**, _albedo or emission color_
        -   **Subsurface**, _the subsurface scale_
        -   **Opacity**, _the opacity of all_
    -   Specular
        -   **Specular**, _the specular of surface_
        -   **Roughness**, _the roughness of surface_
    -   Emission
        -   **Emission**, _the emission strength_

</div>

### 🦠 Slime Shader

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_slime-shader.png)

-   Assign a semi-transparent shader based on the preview mesh with visible inclusions. Does not support cross-section and color ramp.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   Base
        -   **Color**, _albedo or emission color_
        -   **Density**, _the degree of solidity_
        -   **Anisotropy**, _the anisotropy of scatting_
    -   Specular
        -   **Specular**, _the specular of surface_
        -   **Roughness**, _the roughness of surface_
    -   Emission
        -   **Emission**, _the emission strength_

</div>

### ☁️ Volume Shader

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_volume-shader.png)

-   Assign a volume-based shader with support for cross-section and color ramp.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   Base
        -   **Color**, _albedo or emission color_
        -   **Density**, _the degree of solidity_
        -   **Anisotropy**, _the anisotropy of scatting_
    -   Emission
        -   **Emission**, _the emission strength_

</div>

### 🔬 Universal Shader

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_universal-shader.png)

-   Assign a ultimate shader, supporting all features of Bioxel Nodes. Of course, the price is slow rendering, which can be greatly improved by adjusting the Volumes > Step Rate to 100 in the Render Settings Panel.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   Base
        -   **Color**, _albedo or emission color_
        -   **Density**, _the degree of solidity_
        -   **Anisotropy**, _the anisotropy of scatting_
    -   Specular
        -   **Specular**, _the specular of surface_
        -   **Roughness**, _the roughness of surface_
    -   Emission
        -   **Emission**, _the emission strength_

</div>

## Cutters

### 🪚 Cut

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_cut.png)

-   Execute all cutters on one component.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   **Cutter 0~4**, _the cutters_
    -   **Hide Guide**, _hide the cutter guide_

</div>


### 🧀 Plane Object Cutter

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_plane-object-cutter.png)

-   Also a plane cutter, but origin and direction are based on exist object.

    ***

    Node Parameter:

    -   **Plane**, _the plane object_
    -   Guide
        -   **Show**, _show the cutter guide_
        -   **Scale**, _scale the cutter guide_

</div>

## Colors

### 🎨 Color Presents

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_color-presets.png)

-   Set color from presets.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   **Presets**, _select color presents_
    -   **Fram Min**, _ramp factor lower limit_
    -   **Fram Max**, _ramp factor upper limit_

</div>

### 2️⃣ Color Ramp 2

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_color-ramp-2.png)

-   Set color ramp base on scalar value.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   **Fram Min**, _ramp factor lower limit_
    -   **Fram Max**, _ramp factor upper limit_
    -   Ramp
        -   **Pos0 Color**, _position 0% Color_
        -   **Pos1 Color**, _position 100% Color_
        -   **Gamma**, _non-linear coefficient, the larger the coefficient, the more lower value color_
        -   **Contrast**, _the larger the contrast, the harder color ramp will be_

</div>

### 3️⃣ Color Ramp 3

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_color-ramp-3.png)

-   Set color ramp base on scalar value.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   **Fram Min**, _ramp factor lower limit_
    -   **Fram Max**, _ramp factor upper limit_
    -   Ramp
        -   **Pos0 Color**, _position 0% Color_
        -   **Pos1 Color**, _position 50% Color_
        -   **Pos2 Color**, _position 100% Color_
        -   **Gamma**, _non-linear coefficient, the larger the coefficient, the more lower value color_
        -   **Contrast**, _the larger the contrast, the harder color ramp will be_

</div>

### 4️⃣ Color Ramp 4

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_color-ramp-4.png)

-   Set color ramp base on scalar value.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   **Fram Min**, _ramp factor lower limit_
    -   **Fram Max**, _ramp factor upper limit_
    -   Ramp
        -   **Pos0 Color**, _position 0% Color_
        -   **Pos1 Color**, _position 33.3% Color_
        -   **Pos2 Color**, _position 66.6% Color_
        -   **Pos3 Color**, _position 100% Color_
        -   **Gamma**, _non-linear coefficient, the larger the coefficient, the more lower value color_
        -   **Contrast**, _the larger the contrast, the harder color ramp will be_

</div>

### 5️⃣ Color Ramp 5

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_color-ramp-5.png)

-   Set color ramp base on scalar value.

    ***

    Node Parameter:

    -   **Component**, _the upstream component_
    -   **Fram Min**, _ramp factor lower limit_
    -   **Fram Max**, _ramp factor upper limit_
    -   Ramp
        -   **Pos0 Color**, _position 0% Color_
        -   **Pos1 Color**, _position 25% Color_
        -   **Pos2 Color**, _position 50% Color_
        -   **Pos3 Color**, _position 75% Color_
        -   **Pos4 Color**, _position 100% Color_
        -   **Gamma**, _non-linear coefficient, the larger the coefficient, the more lower value color_
        -   **Contrast**, _the larger the contrast, the harder color ramp will be_

</div>

## Utils

### 📦 Join Component

<div class="grid cards" markdown>

-   ![alt text](assets/nodes_join-component.png)

-   Components' combination should not be done by "Join Geometry" node because Blender Cycles can't render volumes in the same position, so the node will slightly offset all components randomly to avoid this problem.

    ***

    Node Parameter:

    -   **Component 0~4**, _the components_

</div>
