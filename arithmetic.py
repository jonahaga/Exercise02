




<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Hackbright-Curriculum/Exercise02/arithmetic.py at master · hackbrightacademy/Hackbright-Curriculum · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="hackbrightacademy/Hackbright-Curriculum" name="twitter:title" /><meta content="Hackbright-Curriculum - Exercises for the Hackbright Academy Fellowship Program" name="twitter:description" /><meta content="https://0.gravatar.com/avatar/65a303cae88fe83d25c9ffa27db10831?d=https%3A%2F%2Fidenticons.github.com%2F5cd11f27e50571af3a71a20fa967c1df.png&amp;r=x&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://0.gravatar.com/avatar/65a303cae88fe83d25c9ffa27db10831?d=https%3A%2F%2Fidenticons.github.com%2F5cd11f27e50571af3a71a20fa967c1df.png&amp;r=x&amp;s=400" property="og:image" /><meta content="hackbrightacademy/Hackbright-Curriculum" property="og:title" /><meta content="https://github.com/hackbrightacademy/Hackbright-Curriculum" property="og:url" /><meta content="Hackbright-Curriculum - Exercises for the Hackbright Academy Fellowship Program" property="og:description" />

    <meta name="hostname" content="github-fe139-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 2.1.0p0-github-tcmalloc (87d8860372) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="32B82ABC:53AF:1DCAF01:52F29750" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="oIQQuMDqTyXkJUxAbbxoVwd9wg71v3fzBwUyKeLNv0c=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-71564d84c77aaffaa3f004e2616af4a1113b044b.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-9435e6151d831c7c0ea851d5963b20db08f8b3d0.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://github.global.ssl.fastly.net/assets/frameworks-6629588efc908265e5f194016e81140bfa95e9ee.js" type="text/javascript"></script>
      <script async="async" defer="defer" src="https://github.global.ssl.fastly.net/assets/github-ab273a0202e49e595f9934f53e64bd784939ea3b.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="8447cdbc95f8302777cddcad10da94f0">

        <link data-pjax-transient rel='permalink' href='/hackbrightacademy/Hackbright-Curriculum/blob/a9bbb01f6338e3c1d7517f9143d9d731a685ff6f/Exercise02/arithmetic.py'>

  <meta name="description" content="Hackbright-Curriculum - Exercises for the Hackbright Academy Fellowship Program" />

  <meta content="6164130" name="octolytics-dimension-user_id" /><meta content="hackbrightacademy" name="octolytics-dimension-user_login" /><meta content="15881058" name="octolytics-dimension-repository_id" /><meta content="hackbrightacademy/Hackbright-Curriculum" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="true" name="octolytics-dimension-repository_is_fork" /><meta content="5708758" name="octolytics-dimension-repository_parent_id" /><meta content="chriszf/Hackbright-Curriculum" name="octolytics-dimension-repository_parent_nwo" /><meta content="5708758" name="octolytics-dimension-repository_network_root_id" /><meta content="chriszf/Hackbright-Curriculum" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/hackbrightacademy/Hackbright-Curriculum/commits/master.atom" rel="alternate" title="Recent Commits to Hackbright-Curriculum:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production linux vis-public fork page-blob">
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fhackbrightacademy%2FHackbright-Curriculum%2Fblob%2Fmaster%2FExercise02%2Farithmetic.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="hackbrightacademy/Hackbright-Curriculum"
      data-branch="master"
      data-sha="5568e10dca650ec0c877292202cbd75b74031804"
  >

    <input type="hidden" name="nwo" value="hackbrightacademy/Hackbright-Curriculum" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fhackbrightacademy%2FHackbright-Curriculum"
    class="minibutton with-count js-toggler-target star-button tooltipped upwards"
    title="You must be signed in to use this feature" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/hackbrightacademy/Hackbright-Curriculum/stargazers">
      0
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fhackbrightacademy%2FHackbright-Curriculum"
        class="minibutton with-count js-toggler-target fork-button tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/hackbrightacademy/Hackbright-Curriculum/network" class="social-count">
        41
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/hackbrightacademy" class="url fn" itemprop="url" rel="author"><span itemprop="title">hackbrightacademy</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/hackbrightacademy/Hackbright-Curriculum" class="js-current-repository js-repo-home-link">Hackbright-Curriculum</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

            <span class="fork-flag">
              <span class="text">forked from <a href="/chriszf/Hackbright-Curriculum">chriszf/Hackbright-Curriculum</a></span>
            </span>
        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      

      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped leftwards" title="Code">
        <a href="/hackbrightacademy/Hackbright-Curriculum" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /hackbrightacademy/Hackbright-Curriculum">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


      <li class="tooltipped leftwards" title="Pull Requests">
        <a href="/hackbrightacademy/Hackbright-Curriculum/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /hackbrightacademy/Hackbright-Curriculum/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/hackbrightacademy/Hackbright-Curriculum/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_wiki /hackbrightacademy/Hackbright-Curriculum/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/hackbrightacademy/Hackbright-Curriculum/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /hackbrightacademy/Hackbright-Curriculum/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/hackbrightacademy/Hackbright-Curriculum/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /hackbrightacademy/Hackbright-Curriculum/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/hackbrightacademy/Hackbright-Curriculum/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /hackbrightacademy/Hackbright-Curriculum/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/hackbrightacademy/Hackbright-Curriculum.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/hackbrightacademy/Hackbright-Curriculum.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/hackbrightacademy/Hackbright-Curriculum" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/hackbrightacademy/Hackbright-Curriculum" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



                <a href="/hackbrightacademy/Hackbright-Curriculum/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:8e47c1be20a97158a523f08834898ed1 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/hackbrightacademy/Hackbright-Curriculum/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/hackbrightacademy/Hackbright-Curriculum/blob/gitoperations/Exercise02/arithmetic.py"
                 data-name="gitoperations"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="gitoperations">gitoperations</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/hackbrightacademy/Hackbright-Curriculum/blob/master/Exercise02/arithmetic.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/hackbrightacademy/Hackbright-Curriculum" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Hackbright-Curriculum</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise02" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Exercise02</span></a></span><span class="separator"> / </span><strong class="final-path">arithmetic.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="Exercise02/arithmetic.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit file-history-tease">
    <img alt="Christian Fernandez" class="main-avatar" height="24" src="https://0.gravatar.com/avatar/e1e11da4339d89e39aacd43e02da3056?d=https%3A%2F%2Fidenticons.github.com%2Ff69d6939f86cba2651b15214fb4f285e.png&amp;r=x&amp;s=140" width="24" />
    <span class="author"><a href="/chriszf" rel="author">chriszf</a></span>
    <time class="js-relative-date" data-title-format="YYYY-MM-DD HH:mm:ss" datetime="2013-03-06T09:23:29-08:00" title="2013-03-06 09:23:29">March 06, 2013</time>
    <div class="commit-title">
        <a href="/hackbrightacademy/Hackbright-Curriculum/commit/b782a20c2b82d125c704fa6880e318ad5c1cadb8" class="message" data-pjax="true" title="Fixing arithmetic.py and calculator.pyc">Fixing arithmetic.py and calculator.pyc</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>2</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="chriszf" href="/hackbrightacademy/Hackbright-Curriculum/commits/master/Exercise02/arithmetic.py?author=chriszf"><img alt="Christian Fernandez" height="20" src="https://0.gravatar.com/avatar/e1e11da4339d89e39aacd43e02da3056?d=https%3A%2F%2Fidenticons.github.com%2Ff69d6939f86cba2651b15214fb4f285e.png&amp;r=x&amp;s=140" width="20" /></a>
    <a class="avatar tooltipped downwards" title="lizTheDeveloper" href="/hackbrightacademy/Hackbright-Curriculum/commits/master/Exercise02/arithmetic.py?author=lizTheDeveloper"><img alt="Liz Howard" height="20" src="https://0.gravatar.com/avatar/a88001c7325ab020b1c8698f2ce2fb6e?d=https%3A%2F%2Fidenticons.github.com%2Fde6466e58cab233a6d649b0ace6c598c.png&amp;r=x&amp;s=140" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Christian Fernandez" height="24" src="https://0.gravatar.com/avatar/e1e11da4339d89e39aacd43e02da3056?d=https%3A%2F%2Fidenticons.github.com%2Ff69d6939f86cba2651b15214fb4f285e.png&amp;r=x&amp;s=140" width="24" />
            <a href="/chriszf">chriszf</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Liz Howard" height="24" src="https://0.gravatar.com/avatar/a88001c7325ab020b1c8698f2ce2fb6e?d=https%3A%2F%2Fidenticons.github.com%2Fde6466e58cab233a6d649b0ace6c598c.png&amp;r=x&amp;s=140" width="24" />
            <a href="/lizTheDeveloper">lizTheDeveloper</a>
          </li>
      </ul>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>24 lines (16 sloc)</span>
        <span>0.259 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped leftwards" href="#"
                 title="You must be signed in to make or propose changes">Edit</a>
          <a href="/hackbrightacademy/Hackbright-Curriculum/raw/master/Exercise02/arithmetic.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/hackbrightacademy/Hackbright-Curriculum/blame/master/Exercise02/arithmetic.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/hackbrightacademy/Hackbright-Curriculum/commits/master/Exercise02/arithmetic.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped leftwards" href="#"
             title="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff tab-size-8">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>

            </td>
            <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="k">def</span> <span class="nf">add</span><span class="p">(</span><span class="n">num1</span><span class="p">,</span> <span class="n">num2</span><span class="p">):</span></div><div class='line' id='LC2'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="mi">10</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="k">def</span> <span class="nf">subtract</span><span class="p">(</span><span class="n">num1</span><span class="p">,</span> <span class="n">num2</span><span class="p">):</span></div><div class='line' id='LC5'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC6'><br/></div><div class='line' id='LC7'><span class="k">def</span> <span class="nf">multiply</span><span class="p">(</span><span class="n">num1</span><span class="p">,</span> <span class="n">num2</span><span class="p">):</span></div><div class='line' id='LC8'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC9'><br/></div><div class='line' id='LC10'><span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">num1</span><span class="p">,</span> <span class="n">num2</span><span class="p">):</span></div><div class='line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="k">def</span> <span class="nf">square</span><span class="p">(</span><span class="n">num1</span><span class="p">):</span></div><div class='line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="k">def</span> <span class="nf">cube</span><span class="p">(</span><span class="n">num1</span><span class="p">):</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="k">def</span> <span class="nf">power</span><span class="p">(</span><span class="n">num1</span><span class="p">,</span> <span class="n">num2</span><span class="p">):</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'><span class="k">def</span> <span class="nf">mod</span><span class="p">(</span><span class="n">num1</span><span class="p">,</span> <span class="n">num2</span><span class="p">):</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div></pre></div></td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.02410s from github-fe139-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/hackbrightacademy/Hackbright-Curriculum/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

