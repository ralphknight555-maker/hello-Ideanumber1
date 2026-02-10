import time
from io import BytesIO
from pathlib import Path

import streamlit as st
from PIL import Image, ImageEnhance

st.set_page_config(page_title="She-Hulk Transformation Game", page_icon="💚", layout="centered")


REFERENCE_IMAGE_CANDIDATES = [
    Path("assets/jennifer_walters_reference.png"),
    Path("assets/jennifer_walters_reference.jpg"),
    Path("assets/jennifer_walters_reference.jpeg"),
]


def load_reference_image(uploaded_file) -> Image.Image | None:
    """Load Jennifer Walters reference image from upload or local assets path."""
    if uploaded_file is not None:
        return Image.open(BytesIO(uploaded_file.read())).convert("RGB")

    for candidate in REFERENCE_IMAGE_CANDIDATES:
        if candidate.exists():
            return Image.open(candidate).convert("RGB")

    return None


def she_hulk_transform(base_image: Image.Image, progress_value: float) -> Image.Image:
    """Create a progressive photo-based transformation effect toward She-Hulk."""
    image = base_image.copy().convert("RGB")

    contrast = ImageEnhance.Contrast(image).enhance(1.0 + 0.35 * progress_value)
    saturation = ImageEnhance.Color(contrast).enhance(1.0 + 0.55 * progress_value)
    brightness = ImageEnhance.Brightness(saturation).enhance(1.0 + 0.08 * progress_value)

    r, g, b = brightness.split()

    r = r.point(lambda px: int(px * (1 - 0.28 * progress_value)))
    g = g.point(lambda px: min(255, int(px * (1 + 0.45 * progress_value))))
    b = b.point(lambda px: int(px * (1 - 0.18 * progress_value)))

    transformed = Image.merge("RGB", (r, g, b))

    aura = Image.new("RGB", transformed.size, color=(80, 255, 130))
    aura_blend = Image.blend(transformed, aura, alpha=0.08 + 0.18 * progress_value)

    zoom = 1.0 + 0.06 * progress_value
    new_w = int(aura_blend.width / zoom)
    new_h = int(aura_blend.height / zoom)
    left = (aura_blend.width - new_w) // 2
    top = (aura_blend.height - new_h) // 2
    cropped = aura_blend.crop((left, top, left + new_w, top + new_h))

    return cropped.resize(aura_blend.size, Image.Resampling.LANCZOS)


st.title("💚 She-Hulk Transformation Game")
st.write("Use your provided Jennifer Walters photo as the base visual, pick an outfit, and control fast or slow transformation speed.")

st.subheader("1) Jennifer Walters reference photo")
uploaded_reference = st.file_uploader(
    "Optional: upload the Jennifer Walters image",
    type=["png", "jpg", "jpeg"],
    help="If you don't upload one, the app will look for assets/jennifer_walters_reference.png",
)

reference_image = load_reference_image(uploaded_reference)

if reference_image is None:
    st.warning(
        "No Jennifer reference photo found yet. Add your provided image via uploader or place it at assets/jennifer_walters_reference.png."
    )

st.subheader("2) Choose your style")
outfit_options = {
    "Courtroom Professional": "Silver-blue blazer and skirt with confident legal flair.",
    "Heroic Suit": "Flexible super-suit built for action.",
    "Casual Street": "Jacket, jeans, and ready-for-anything energy.",
    "Training Gear": "Athletic outfit for focused strength training.",
    "Evening Gala": "Elegant red-carpet look with superhero attitude.",
    "Lab Scientist": "Lab coat, safety goggles, and gamma smarts.",
    "Stealth Ops": "Dark tactical suit made for night missions.",
    "Beach Day": "Bright summer style for heroic downtime.",
    "Retro 80s": "Bold neon power look from another era.",
    "Battle Armor": "Reinforced armor plating for heavy combat.",
    "Gamma Executive": "Power suit inspired by Jennifer's reference look.",
    "Power Advocate": "Courtroom-chic with extra superhero edge.",
}
selected_outfit = st.selectbox("Outfit", list(outfit_options.keys()))
st.caption(outfit_options[selected_outfit])

st.subheader("3) Set transformation speed")
speed = st.radio("Speed", ["Fast", "Slow"], horizontal=True)

speed_settings = {
    "Fast": {"delay": 0.25, "steps": 6},
    "Slow": {"delay": 0.8, "steps": 10},
}

st.subheader("4) Select mode")
mode = st.radio("Mode", ["Story Mode", "Sandbox Mode"], horizontal=True)

if "sandbox_progress" not in st.session_state:
    st.session_state.sandbox_progress = 0.0

status = st.empty()
progress = st.progress(0)
stage_box = st.empty()
visual_box = st.empty()


def render_progress_frame(base_image: Image.Image, progress_value: float, outfit_name: str):
    label = "Jennifer Walters" if progress_value < 0.5 else "She-Hulk"
    transformed_frame = she_hulk_transform(base_image, progress_value)
    visual_box.image(
        transformed_frame,
        caption=f"{label} ({outfit_name}) • Transformation progress: {int(progress_value * 100)}%",
        use_container_width=True,
    )


if reference_image is not None and mode == "Sandbox Mode":
    st.write("### 🧪 Sandbox Controls")
    st.write("Transform Jennifer to and from She-Hulk as many times as you want.")

    sandbox_frame = she_hulk_transform(reference_image, st.session_state.sandbox_progress)
    st.image(
        sandbox_frame,
        caption=f"Sandbox preview: {int(st.session_state.sandbox_progress * 100)}%",
        use_container_width=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Transform to She-Hulk ⬆️", use_container_width=True):
            st.session_state.sandbox_progress = 1.0
            st.rerun()
    with col2:
        if st.button("Transform to Jennifer ⬇️", use_container_width=True):
            st.session_state.sandbox_progress = 0.0
            st.rerun()
    with col3:
        if st.button("Toggle Form 🔁", use_container_width=True):
            st.session_state.sandbox_progress = 0.0 if st.session_state.sandbox_progress >= 0.5 else 1.0
            st.rerun()

    slider_progress = st.slider(
        "Manual transformation control",
        min_value=0,
        max_value=100,
        value=int(st.session_state.sandbox_progress * 100),
        step=1,
    )
    st.session_state.sandbox_progress = slider_progress / 100

    current_form = "She-Hulk" if st.session_state.sandbox_progress >= 0.5 else "Jennifer Walters"
    st.success(f"Current sandbox form: **{current_form}**")

if mode == "Story Mode":
    st.subheader("5) Begin story transformation")
    start = st.button("Start Transformation ⚡", type="primary")

    if start:
        if reference_image is None:
            status.error("Please provide the Jennifer Walters reference image first.")
        else:
            settings = speed_settings[speed]
            total_steps = settings["steps"]

            stages = [
                "Jennifer steadies her breathing...",
                "Gamma energy builds around her silhouette.",
                "Her strength and posture begin to shift.",
                "Muscles surge with controlled power.",
                "Final green-energy spike!",
                "She-Hulk mode activated! 💥",
            ]

            status.info(f"Outfit selected: **{selected_outfit}** | Transformation speed: **{speed}**")

            for i in range(1, total_steps + 1):
                current_progress = i / total_steps
                progress.progress(current_progress)

                stage_index = min(int(current_progress * (len(stages) - 1)), len(stages) - 1)
                stage_box.markdown(f"### {stages[stage_index]}")

                render_progress_frame(reference_image, current_progress, selected_outfit)
                time.sleep(settings["delay"])

            status.success("Transformation complete! She-Hulk is ready to save the day.")

st.divider()
st.write("### 🎮 Mini Challenge")
mission = st.selectbox(
    "Pick a mission",
    ["Courtroom Showdown", "City Rescue", "Rooftop Training", "Gamma Lab Emergency"],
)

if st.button("Launch Mission"):
    st.balloons()
    st.success(f"Mission launched: **{mission}** with **{selected_outfit}** style!")
