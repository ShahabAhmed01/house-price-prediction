# California House Price Prediction Demo Script

**Video Purpose**: Showcase geospatial data visualization and ensemble regression models.
**Target Duration**: 60-90 seconds
**Format**: Screen recording with voiceover (Loom, OBS, Supademo)

---

## 🎬 Script & Cues

### 1. Introduction (0:00 - 0:15)
**Visual**: Show the `README.md` and the project structure in VS Code/GitHub.
**Voiceover**: 
> "Hi, I'm Shahab Ahmed. For Task 6 of my AI/ML Internship at DevelopersHub Corporation, I was tasked with predicting the median house values in California using a mix of demographic, economic, and geospatial data."

### 2. Geospatial EDA (0:15 - 0:40)
**Visual**: Show `01-target-distribution.png`, then smoothly transition to `02-geographic-distribution.png` (the scatter plot mapping coordinates to price).
**Voiceover**: 
> "The most interesting part of this dataset is the geospatial component. By simply plotting the longitude and latitude coordinates of the housing blocks, you can actually see the shape of the California coastline emerge! More importantly, the color gradient highlights a massive price premium for properties located right on the coast or near major hubs like the Bay Area."

### 3. Ensemble Modeling (0:40 - 1:00)
**Visual**: Show the `house_price_prediction.ipynb` notebook scrolling through the Gradient Boosting section. Then show `04-model-predictions.png`.
**Voiceover**: 
> "To capture these complex spatial and demographic relationships, simple linear models weren't enough. I built an ensemble pipeline using a Gradient Boosting Regressor. As you can see in this scatter plot comparing actual versus predicted prices, the model tracks the variance incredibly well, significantly outperforming the baselines."

### 4. Conclusion (1:00 - 1:15)
**Visual**: End on the GitHub repository page or the final metric summary.
**Voiceover**: 
> "This project really proved to me how powerful spatial features are in real estate modeling. Thanks for watching, and feel free to check out my full Jupyter Notebook on GitHub!"
