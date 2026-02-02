"""
Gradio demo: embed4d custom HTML viewer vs Gradio built-in Model3D.

Run: python examples/demo_gradio.py
Requires: pip install embed4d[gradio]  (or pip install gradio)
"""

import gradio as gr

from embed4d import model3d_viewer

HEIGHT = 500


def update_viewers(file):
    """Update custom HTML viewer and Gradio Model3D when a file is selected."""
    if file is None:
        custom_html = model3d_viewer(None, height=HEIGHT)
        return custom_html, None
    path = file.name if hasattr(file, "name") else file
    custom_html = model3d_viewer(path, height=HEIGHT)
    return custom_html, path


with gr.Blocks(title="embed4d vs Gradio Model3D", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        "### Compare: **embed4d** HTML viewer vs Gradio **Model3D**\n\n"
        "Upload a GLB/GLTF/FBX file to see both viewers side by side."
    )
    file_input = gr.File(
        file_types=[".glb", ".gltf", ".fbx"],
        label="Select 3D model (GLB / GLTF / FBX)",
        type="filepath",
    )

    with gr.Row(height=HEIGHT):
        with gr.Column():
            gr.Markdown("**embed4d** — custom HTML viewer (Three.js)")
            custom_viewer = gr.HTML(value=model3d_viewer(None, height=HEIGHT))
        with gr.Column():
            gr.Markdown("**Gradio** — built-in `gr.Model3D`")
            gradio_viewer = gr.Model3D(label="Model3D", height=HEIGHT)

    file_input.change(
        fn=update_viewers,
        inputs=file_input,
        outputs=[custom_viewer, gradio_viewer],
    )


if __name__ == "__main__":
    demo.launch()
