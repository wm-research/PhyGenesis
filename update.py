import os

html_content = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="description" content="PhyGenesis: Toward Physically Consistent Driving Video World Models under Challenging Trajectories.">
  <meta name="keywords" content="Autonomous driving, World models, Video generation">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PhyGenesis</title>
  <link rel="stylesheet" href="./static/css/bulma.min.css">
  <link rel="stylesheet" href="./static/css/fontawesome.all.min.css">
  <link rel="stylesheet" href="./static/css/index.css">
</head>
<body>

<section class="hero">
  <div class="hero-body">
    <div class="container is-max-desktop">
      <div class="columns is-centered">
        <div class="column has-text-centered">
          <h1 class="title is-1 publication-title">Toward Physically Consistent Driving Video World Models under Challenging Trajectories</h1>
          
          <div class="is-size-5 publication-authors">
            <span class="author-block">Jiawei Zhou<sup>1,2*</sup>,</span>
            <span class="author-block">Zhenxin Zhu<sup>2*</sup>,</span>
            <span class="author-block">Lingyi Du<sup>1*</sup>,</span>
            <span class="author-block">Linye Lyu<sup>3</sup>,</span>
            <span class="author-block">Lijun Zhou<sup>2</sup>,</span>
            <span class="author-block">Zhanqian Wu<sup>2</sup>,</span>
            <span class="author-block">Hongcheng Luo<sup>2</sup>,</span>
            <span class="author-block">Zhuotao Tian<sup>4</sup>,</span>
            <span class="author-block">Bing Wang<sup>2</sup>,</span>
            <span class="author-block">Guang Chen<sup>2</sup>,</span>
            <span class="author-block">Haiyang Sun<sup>2?</sup>,</span>
            <span class="author-block">Hangjun Ye<sup>2?</sup>,</span>
            <span class="author-block">Yu Li<sup>1</sup></span>
          </div>

          <div class="is-size-5 publication-authors">
            <span class="author-block"><sup>1</sup>Zhejiang University,</span>
            <span class="author-block"><sup>2</sup>Xiaomi EV,</span>
            <span class="author-block"><sup>3</sup>The Hong Kong Polytechnic University,</span>
            <span class="author-block"><sup>4</sup>Shenzhen Loop Area Institute</span>
          </div>
          
          <div class="is-size-6 publication-authors mt-2">
            <span class="author-block"><sup>*</sup>Equal Contribution, <sup>?</sup>Project Leader, <sup>?</sup>Corresponding Author</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="hero teaser">
  <div class="container is-max-desktop">
    <div class="hero-body has-text-centered">
      <img src="./static/images/teaser.png" alt="Teaser" style="width: 100%; border-radius: 8px;">
      <h2 class="subtitle mt-4">
        Qualitative comparison of video generation under diverse trajectory conditions. PhyGenesis preserves physical consistency and high visual fidelity.
      </h2>
    </div>
  </div>
</section>

<section class="section">
  <div class="container is-max-desktop">
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <h2 class="title is-3">Abstract</h2>
        <div class="content has-text-justified">
          <p>
            Video generation models have shown strong potential as world models for autonomous driving simulation. However, existing approaches are primarily trained on real-world driving datasets, which mostly contain natural and safe driving scenarios. As a result, current models often fail when conditioned on challenging or counterfactual trajectories. To address this limitation, we propose <strong>PhyGenesis</strong>, a world model designed to generate driving videos with high visual fidelity and strong physical consistency.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container is-max-desktop">
    <div class="columns is-centered has-text-centered">
      <div class="column is-full-width">
        <h2 class="title is-3">Method Overview</h2>
        <img src="./static/images/framework.png" alt="Framework" style="width: 100%; border-radius: 8px;">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container is-max-desktop">
    <h2 class="title is-3 has-text-centered">Quantitative Results</h2>
    <div class="columns is-centered mt-4">
      <div class="column is-full-width has-text-centered">
        <img src="./static/images/Table1.png" alt="Table 1" style="width: 100%; max-width: 900px;">
      </div>
    </div>
    <div class="columns is-centered mt-5">
      <div class="column is-full-width has-text-centered">
        <img src="./static/images/Table2.png" alt="Table 2" style="width: 100%; max-width: 900px;">
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container is-max-desktop">
    <h2 class="title is-3 has-text-centered">Video Generation Comparisons</h2>

    <div class="columns is-centered mt-5">
      <div class="column is-full-width">
        <h3 class="title is-4">Versus High-quality Baselines (Fig. 5)</h3>
        <div class="columns is-centered">
          <div class="column"><video playsinline autoplay loop muted controls style="border-radius: 10px; width: 100%;"><source src="./static/videos/fig5.mp4" type="video/mp4"></video></div>
        </div>
      </div>
    </div>

    <div class="columns is-centered mt-5">
      <div class="column is-full-width">
        <h3 class="title is-4">Trajectory Correction (Fig. 8)</h3>
        <div class="columns is-vcentered is-centered">
          <div class="column has-text-centered">
            <h4 class="title is-5">Input Trajectories</h4>
            <video playsinline autoplay loop muted controls style="border-radius: 10px; width: 100%;"><source src="./static/videos/fig8_in.mp4" type="video/mp4"></video>
          </div>
          <div class="column has-text-centered">
            <h4 class="title is-5">Output Trajectories</h4>
            <video playsinline autoplay loop muted controls style="border-radius: 10px; width: 100%;"><source src="./static/videos/fig8_out.mp4" type="video/mp4"></video>
          </div>
        </div>
      </div>
    </div>

    <div class="columns is-centered mt-5">
      <div class="column is-full-width">
        <h3 class="title is-4">Ablation Study: Heterogeneous Data (Fig. 10)</h3>
        <div class="columns is-vcentered is-centered">
          <div class="column has-text-centered">
            <h4 class="title is-5">Without Heterogeneous Data</h4>
            <video playsinline autoplay loop muted controls style="border-radius: 10px; width: 100%;"><source src="./static/videos/fig10_wo.mp4" type="video/mp4"></video>
          </div>
          <div class="column has-text-centered">
            <h4 class="title is-5">With Heterogeneous Data</h4>
            <video playsinline autoplay loop muted controls style="border-radius: 10px; width: 100%;"><source src="./static/videos/fig10_with.mp4" type="video/mp4"></video>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

</body>
</html>"""

with open(r"c:\Users\MI\Desktop\Phygenesis\OpenSource\PhyGenesis_Web\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

readme_content = """# PhyGenesis: Toward Physically Consistent Driving Video World Models under Challenging Trajectories

Video generation models have shown strong potential as world models for autonomous driving simulation. However, existing approaches are primarily trained on real-world driving datasets, which mostly contain natural and safe driving scenarios. As a result, current models often fail when conditioned on challenging or counterfactual trajectories.

To address this limitation, we propose **PhyGenesis**, a world model designed to generate driving videos with high visual fidelity and strong physical consistency.
"""

with open(r"c:\Users\MI\Desktop\Phygenesis\OpenSource\PhyGenesis_Web\README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

