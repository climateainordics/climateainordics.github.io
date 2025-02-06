<label for="tagFilter">Filter affiliates:</label>
<select id="tagFilter">
<option value="all">Show All</option>
<option value="Bayesian Optimisation">Bayesian Optimisation</option>
<option value="Biodiversity">Biodiversity</option>
<option value="Climate Impacts">Climate Impacts</option>
<option value="Climate Modeling">Climate Modeling</option>
<option value="Climate Policy">Climate Policy</option>
<option value="Computer Vision">Computer Vision</option>
<option value="Deep Learning">Deep Learning</option>
<option value="Earth Observation">Earth Observation</option>
<option value="Ecosystem Monitoring And Modelling">Ecosystem Monitoring And Modelling</option>
<option value="Education">Education</option>
<option value="Efficient Or Sustainable Ai">Efficient Or Sustainable Ai</option>
<option value="Environment Impacts Of Ai">Environment Impacts Of Ai</option>
<option value="Extreme Weather">Extreme Weather</option>
<option value="Fluid Dynamics">Fluid Dynamics</option>
<option value="Geomatics">Geomatics</option>
<option value="Gis">Gis</option>
<option value="Hpc">Hpc</option>
<option value="Impact On Climate Change On Health">Impact On Climate Change On Health</option>
<option value="Knowledge Graphs">Knowledge Graphs</option>
<option value="Machine Learning">Machine Learning</option>
<option value="Machine Listening">Machine Listening</option>
<option value="Marine Ecology">Marine Ecology</option>
<option value="Materials And Atmospheric Science">Materials And Atmospheric Science</option>
<option value="Meteorology">Meteorology</option>
<option value="Molecular Modeling Of Atmospheric Chemistry">Molecular Modeling Of Atmospheric Chemistry</option>
<option value="Nlp">Nlp</option>
<option value="Remote Sensing">Remote Sensing</option>
<option value="Soundscape Analysis">Soundscape Analysis</option>
<option value="Spatial Analysis">Spatial Analysis</option>
<option value="Sustainable Cities">Sustainable Cities</option>
<option value="Sustainable Production">Sustainable Production</option>
<option value="Sustainable Space Exploration And Research">Sustainable Space Exploration And Research</option>
<option value="Sustainable Transport">Sustainable Transport</option>
<option value="Urban Planning">Urban Planning</option>
<option value="Weather Forecasting">Weather Forecasting</option></select>

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

