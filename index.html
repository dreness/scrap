<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="UTF-8">
    <title>Scrap by dreness</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="stylesheets/normalize.css" media="screen">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css" media="screen">
    <link rel="stylesheet" type="text/css" href="stylesheets/github-light.css" media="screen">
  </head>
  <body>
    <section class="page-header">
      <h1 class="project-name">Scrap</h1>
      <h2 class="project-tagline">Lompy stankles, who-da-whatnows, and kaboodle kits.</h2>
      <a href="https://github.com/dreness/scrap" class="btn">View on GitHub</a>
      <a href="https://github.com/dreness/scrap/zipball/master" class="btn">Download .zip</a>
      <a href="https://github.com/dreness/scrap/tarball/master" class="btn">Download .tar.gz</a>
    </section>

    <section class="main-content">
      <p>This document augments the elk-docker ReadMe to describe the changes made in the dreness-netflow branch. Also included is a brief 'from scratch' setup guide for OS X. If you already have Docker ready, proceed to <a href="#build-the-dreness-netflow-branch-of-elk-dockergit">this section</a>.</p>

<h2>
<a id="os-x-setup" class="anchor" href="#os-x-setup" aria-hidden="true"><span class="octicon octicon-link"></span></a>OS X Setup</h2>

<h3>
<a id="install-homebrew" class="anchor" href="#install-homebrew" aria-hidden="true"><span class="octicon octicon-link"></span></a>install homebrew</h3>

<pre><code>curl -o hb-install.rb -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install
</code></pre>

<p>Look at hb-install.rb, convince yourself you won't get owned by running it, then run it.</p>

<pre><code>ruby hb-install.rb
</code></pre>

<h3>
<a id="install-docker-toolchain" class="anchor" href="#install-docker-toolchain" aria-hidden="true"><span class="octicon octicon-link"></span></a>install docker toolchain</h3>

<pre><code>brew install Caskroom/cask/dockertoolbox
</code></pre>

<h3>
<a id="create-docker-host-called-default" class="anchor" href="#create-docker-host-called-default" aria-hidden="true"><span class="octicon octicon-link"></span></a>create docker host called 'default'</h3>

<pre><code>docker-machine -D create \
                  --driver virtualbox \
                  --virtualbox-cpu-count "4" \
                  --virtualbox-memory "4096" \
                  default
</code></pre>

<h3>
<a id="add-nat-port-maps-in-docker-host-for-netflow-and-kibana" class="anchor" href="#add-nat-port-maps-in-docker-host-for-netflow-and-kibana" aria-hidden="true"><span class="octicon octicon-link"></span></a>Add NAT port maps in docker host for netflow and kibana</h3>

<pre><code>docker-machine stop default
VBoxManage modifyvm "default" --natpf1 "kibana,tcp,,5601,,5601"
VBoxManage modifyvm "default" --natpf1 "netflow,udp,,9995,,9995"
docker-machine start default
</code></pre>

<h3>
<a id="verify-that-its-up-by-sshing-to-it" class="anchor" href="#verify-that-its-up-by-sshing-to-it" aria-hidden="true"><span class="octicon octicon-link"></span></a>Verify that it's up by SSH'ing to it</h3>

<pre><code>docker-machine ssh default
</code></pre>

<p>(log out of SSH)</p>

<h4>
<a id="prepare-shell-for-docker-use" class="anchor" href="#prepare-shell-for-docker-use" aria-hidden="true"><span class="octicon octicon-link"></span></a>prepare shell for docker use</h4>

<pre><code>eval "$(docker-machine env default)"
</code></pre>

<h2>
<a id="build-the-dreness-netflow-branch-of-elk-dockergit" class="anchor" href="#build-the-dreness-netflow-branch-of-elk-dockergit" aria-hidden="true"><span class="octicon octicon-link"></span></a>Build the dreness-netflow branch of elk-docker.git</h2>

<h4>
<a id="clone-the-elk-docker-repo-move-into-it-and-build-a-container" class="anchor" href="#clone-the-elk-docker-repo-move-into-it-and-build-a-container" aria-hidden="true"><span class="octicon octicon-link"></span></a>clone the elk-docker repo, move into it, and build a container</h4>

<pre><code>git clone https://github.com/dreness/elk-docker.git
cd elk-docker
git checkout dreness-netflow
docker-compose build elk
docker-compose up
</code></pre>

<p>(you can control-c without killing the container, or leave it open to watch)</p>

<h4>
<a id="arrange-for-your-netflow-data-to-be-sent-to-your-computers-ip-on-udp9995" class="anchor" href="#arrange-for-your-netflow-data-to-be-sent-to-your-computers-ip-on-udp9995" aria-hidden="true"><span class="octicon octicon-link"></span></a>Arrange for your netflow data to be sent to your computer's IP on UDP/9995</h4>

<p>NB: The included dashboard is currently intended for netflow data collected from a single interface. For example, in a typical firewall situation, if data from both the internal and external interfaces is collected, traffic flowing through the router would be double counted. Not sure yet if it's possible to filter out packets collected from a specific interface, as they arrive with nearly identical netflow fields and values - except for byte count, oddly enough... but I digress.</p>

<h4>
<a id="if-you-dont-already-have-a-netflow-probe--exporter-in-mind-use-fprobe" class="anchor" href="#if-you-dont-already-have-a-netflow-probe--exporter-in-mind-use-fprobe" aria-hidden="true"><span class="octicon octicon-link"></span></a>If you don't already have a netflow probe / exporter in mind, use fprobe:</h4>

<pre><code>brew install fprobe
sudo fprobe -v 6 -i en0 -n 5 -f ip -l 2 localhost:9995
</code></pre>

<h4>
<a id="load-the-kibana-web-interface-and-configure-the-index" class="anchor" href="#load-the-kibana-web-interface-and-configure-the-index" aria-hidden="true"><span class="octicon octicon-link"></span></a>Load the kibana web interface and configure the index</h4>

<p><a href="http://localhost:5601/#/settings/indices/?_g=()">http://localhost:5601/#/settings/indices/?_g=()</a></p>

<p>You should be at a 'configure an index pattern' page. Reload the page until the "Time-field name" menu appears (the netflow data can take a minute or two to get started). Choose <a href="https://github.com/timestamp" class="user-mention">@timestamp</a> from it, then click create.</p>

<h4>
<a id="edit-the-format-of-the-bytes-field-to-produce-formatted-output" class="anchor" href="#edit-the-format-of-the-bytes-field-to-produce-formatted-output" aria-hidden="true"><span class="octicon octicon-link"></span></a>Edit the format of the 'bytes' field to produce formatted output.</h4>

<p>Click "settings", then click the "logstash-*" index pattern.
Click the pencil icon adjacent to <code>netflow.in_bytes</code> to edit it.
Set the format to Bytes</p>

<h4>
<a id="import-dashboard-visit-dashboard" class="anchor" href="#import-dashboard-visit-dashboard" aria-hidden="true"><span class="octicon octicon-link"></span></a>Import dashboard, visit dashboard</h4>

<p>Click Settings, then Objects in the second nav bar.
Import the combined.json file, or all of the individual json files.
Click 'Dashboard' in the navbar, then click the 'load saved dashboard' icon to the right of the search field. Select the "Netflow" dashboard.</p>

<p>Enjoy :)</p>

<h2>
<a id="misc" class="anchor" href="#misc" aria-hidden="true"><span class="octicon octicon-link"></span></a>Misc</h2>

<h4>
<a id="restart-a-previous-elk-docker-find-its-name-first" class="anchor" href="#restart-a-previous-elk-docker-find-its-name-first" aria-hidden="true"><span class="octicon octicon-link"></span></a>restart a previous elk-docker. find its name first:</h4>

<pre><code>docker ps -l
docker start &lt;whatever&gt;
</code></pre>

<h4>
<a id="delete-docker-host-the-elk-docker-container-goes-with-it" class="anchor" href="#delete-docker-host-the-elk-docker-container-goes-with-it" aria-hidden="true"><span class="octicon octicon-link"></span></a>Delete docker host. The elk-docker container goes with it.</h4>

<pre><code>docker-machine rm default
</code></pre>

<h4>
<a id="list-containers" class="anchor" href="#list-containers" aria-hidden="true"><span class="octicon octicon-link"></span></a>list containers</h4>

<pre><code>docker ps
</code></pre>

<h4>
<a id="show-nic-info" class="anchor" href="#show-nic-info" aria-hidden="true"><span class="octicon octicon-link"></span></a>show NIC info</h4>

<pre><code>BoxManage showvminfo default --details | egrep 'NIC [12]' 2&gt;&amp;1
</code></pre>

<h4>
<a id="show-docker-host-infos" class="anchor" href="#show-docker-host-infos" aria-hidden="true"><span class="octicon octicon-link"></span></a>show docker host infos</h4>

<pre><code>VBoxManage showvminfo default
VBoxManage list hostonlyifs
</code></pre>

      <footer class="site-footer">
        <span class="site-footer-owner"><a href="https://github.com/dreness/scrap">Scrap</a> is maintained by <a href="https://github.com/dreness">dreness</a>.</span>

        <span class="site-footer-credits">This page was generated by <a href="https://pages.github.com">GitHub Pages</a> using the <a href="https://github.com/jasonlong/cayman-theme">Cayman theme</a> by <a href="https://twitter.com/jasonlong">Jason Long</a>.</span>
      </footer>

    </section>

  
  </body>
</html>
