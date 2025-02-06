<!-- Dropdown for selecting tags -->
<label for="tagFilter">Filter affiliates:</label>
<select id="tagFilter">
<option value="all">Show All</option>
<option value="Bayesian optimisation">Bayesian optimisation</option>

<option value="Biodiversity">Biodiversity</option>

<option value="Climate modeling">Climate modeling</option>

<option value="Computer vision">Computer vision</option>

<option value="Deep Learning.">Deep Learning.</option>

<option value="Deep learning">Deep learning</option>

<option value="Earth observation">Earth observation</option>

<option value="Ecosystem monitoring and modelling">Ecosystem monitoring and modelling</option>

<option value="Efficient or sustainable AI">Efficient or sustainable AI</option>

<option value="Environment impacts of AI">Environment impacts of AI</option>

<option value="Extreme weather">Extreme weather</option>

<option value="Fluid dynamics">Fluid dynamics</option>

<option value="GIS">GIS</option>

<option value="Geomatics">Geomatics</option>

<option value="HPC">HPC</option>

<option value="Impact on climate change on health">Impact on climate change on health</option>

<option value="Knowledge graphs">Knowledge graphs</option>

<option value="Machine Learning">Machine Learning</option>

<option value="Machine Listening">Machine Listening</option>

<option value="Machine learning">Machine learning</option>

<option value="Machine listening">Machine listening</option>

<option value="Marine ecology">Marine ecology</option>

<option value="Molecular modeling of atmospheric chemistry">Molecular modeling of atmospheric chemistry</option>

<option value="NLP">NLP</option>

<option value="Remote sensing">Remote sensing</option>

<option value="Soundscape analysis">Soundscape analysis</option>

<option value="Spatial Analysis">Spatial Analysis</option>

<option value="Sustainable cities">Sustainable cities</option>

<option value="Sustainable production">Sustainable production</option>

<option value="Sustainable space exploration and research">Sustainable space exploration and research</option>

<option value="Sustainable transport">Sustainable transport</option>

<option value="Urban planning">Urban planning</option>

<option value="Weather forecasting">Weather forecasting</option>

<option value="climate impacts">climate impacts</option>

<option value="climate policy">climate policy</option>

<option value="education">education</option>

<option value="materials and atmospheric science">materials and atmospheric science</option>

<option value="meteorology">meteorology</option>

<option value="sustainable cities">sustainable cities</option>

<option value="sustainable production">sustainable production</option>

<option value="urban planning">urban planning</option>

</select>

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

