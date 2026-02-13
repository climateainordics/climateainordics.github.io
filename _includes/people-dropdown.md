<label for="tagFilter">Filter people:</label>
<select id="tagFilter">
<option value="all">Show All</option>
<option value="AI">AI (1)</option>
<option value="AI For Climate Education">AI For Climate Education (1)</option>
<option value="Amortized Inference">Amortized Inference (1)</option>
<option value="Atmospheric Science">Atmospheric Science (1)</option>
<option value="AutoML">AutoML (10)</option>
<option value="Bayesian Inference">Bayesian Inference (1)</option>
<option value="Bayesian Optimisation">Bayesian Optimisation (19)</option>
<option value="Biodiversity">Biodiversity (78)</option>
<option value="Bioinformatics">Bioinformatics (1)</option>
<option value="Causal AI">Causal AI (1)</option>
<option value="Climate Impacts">Climate Impacts (47)</option>
<option value="Climate Modeling">Climate Modeling (86)</option>
<option value="Climate Policy">Climate Policy (1)</option>
<option value="Computer Vision">Computer Vision (93)</option>
<option value="Cryospheric Science">Cryospheric Science (1)</option>
<option value="Data Assimilation">Data Assimilation (2)</option>
<option value="Deep Learning">Deep Learning (137)</option>
<option value="Disaster Management">Disaster Management (1)</option>
<option value="Drought">Drought (1)</option>
<option value="Earth Observation">Earth Observation (107)</option>
<option value="Earth System Modeling">Earth System Modeling (30)</option>
<option value="Ecosystem Monitoring and Modelling">Ecosystem Monitoring and Modelling (1)</option>
<option value="Ecosystem Services">Ecosystem Services (1)</option>
<option value="Ecosystem-based Adaptation">Ecosystem-based Adaptation (1)</option>
<option value="Edna">Edna (1)</option>
<option value="Education">Education (1)</option>
<option value="Efficient or Sustainable AI">Efficient or Sustainable AI (74)</option>
<option value="Emulators">Emulators (1)</option>
<option value="Environment Impacts of AI">Environment Impacts of AI (1)</option>
<option value="Extreme Weather">Extreme Weather (2)</option>
<option value="Extreme Weather Events">Extreme Weather Events (29)</option>
<option value="Fluid Dynamics">Fluid Dynamics (1)</option>
<option value="Food Microbiology">Food Microbiology (1)</option>
<option value="Forest">Forest (1)</option>
<option value="Forest Projection">Forest Projection (1)</option>
<option value="Fracture Mechanics">Fracture Mechanics (1)</option>
<option value="GIS">GIS (2)</option>
<option value="Gaussian Processes">Gaussian Processes (1)</option>
<option value="Generative-ai; Climate Futures; Spatial Imaginaries">Generative-ai; Climate Futures; Spatial Imaginaries (1)</option>
<option value="Geomatics">Geomatics (1)</option>
<option value="HPC">HPC (1)</option>
<option value="Hybrid Methods">Hybrid Methods (1)</option>
<option value="Hydrology">Hydrology (1)</option>
<option value="Ice Sheet–climate Interaction">Ice Sheet–climate Interaction (1)</option>
<option value="Impact on Climate Change on Health">Impact on Climate Change on Health (1)</option>
<option value="Inverse Modeling">Inverse Modeling (1)</option>
<option value="Knowledge Graphs">Knowledge Graphs (1)</option>
<option value="Land System Science">Land System Science (1)</option>
<option value="Land Use Change Modelling">Land Use Change Modelling (1)</option>
<option value="Machine Learning">Machine Learning (163)</option>
<option value="Machine Listening">Machine Listening (2)</option>
<option value="Marine Ecology">Marine Ecology (25)</option>
<option value="Materials">Materials (1)</option>
<option value="Metagenomics">Metagenomics (1)</option>
<option value="Meteorology">Meteorology (1)</option>
<option value="Molecular Modeling of Atmospheric Chemistry">Molecular Modeling of Atmospheric Chemistry (2)</option>
<option value="NLP">NLP (35)</option>
<option value="Nature-based Solutions">Nature-based Solutions (1)</option>
<option value="Numerical Weather Prediction">Numerical Weather Prediction (1)</option>
<option value="Oceanography">Oceanography (1)</option>
<option value="One Health">One Health (1)</option>
<option value="Public Health">Public Health (1)</option>
<option value="Remote Sensing">Remote Sensing (2)</option>
<option value="Simulation-based Inference">Simulation-based Inference (1)</option>
<option value="Solar Energy">Solar Energy (1)</option>
<option value="Soundscape Analysis">Soundscape Analysis (23)</option>
<option value="Spatial Analysis">Spatial Analysis (1)</option>
<option value="Species Distribution Modelling">Species Distribution Modelling (1)</option>
<option value="Stochastic Modelling and Distributions">Stochastic Modelling and Distributions (1)</option>
<option value="Sustainability Science">Sustainability Science (1)</option>
<option value="Sustainable Cities">Sustainable Cities (62)</option>
<option value="Sustainable Energy">Sustainable Energy (18)</option>
<option value="Sustainable Heating">Sustainable Heating (1)</option>
<option value="Sustainable Production">Sustainable Production (32)</option>
<option value="Sustainable Space Exploration and Research">Sustainable Space Exploration and Research (1)</option>
<option value="Sustainable Transport">Sustainable Transport (30)</option>
<option value="Uav">Uav (1)</option>
<option value="Urban Health">Urban Health (1)</option>
<option value="Urban Planning">Urban Planning (42)</option>
<option value="Use of Weather and Climate Data Outside of Academia">Use of Weather and Climate Data Outside of Academia (1)</option>
<option value="Visual Analytics">Visual Analytics (1)</option>
<option value="Visualization">Visualization (1)</option>
<option value="Weather Forecasting">Weather Forecasting (17)</option>
<option value="Wildfire Growth Forecasting">Wildfire Growth Forecasting (1)</option>
<option value="Wind Energy">Wind Energy (12)</option></select>

<script>
        document.getElementById('tagFilter').addEventListener('change', function () {
            const selectedTag = this.value;
            document.querySelectorAll('.content').forEach(div => {
                const tags = div.getAttribute('data-tags').split(',');
                if (selectedTag === 'all' || tags.includes(selectedTag)) {
                    div.classList.remove('hidden');
                } else {
                    div.classList.add('hidden');
                }
            });
        });
</script>

