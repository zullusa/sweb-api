          API Spaceweb - Vps  \[data-simplebar\]{position:relative;flex-direction:column;flex-wrap:wrap;justify-content:flex-start;align-content:flex-start;align-items:flex-start}.simplebar-wrapper{overflow:hidden;width:inherit;height:inherit;max-width:inherit;max-height:inherit}.simplebar-mask{direction:inherit;position:absolute;overflow:hidden;padding:0;margin:0;left:0;top:0;bottom:0;right:0;width:auto!important;height:auto!important;z-index:0}.simplebar-offset{direction:inherit!important;box-sizing:inherit!important;resize:none!important;position:absolute;top:0;left:0;bottom:0;right:0;padding:0;margin:0;-webkit-overflow-scrolling:touch}.simplebar-content-wrapper{direction:inherit;box-sizing:border-box!important;position:relative;display:block;height:100%;width:auto;max-width:100%;max-height:100%;scrollbar-width:none;-ms-overflow-style:none}.simplebar-content-wrapper::-webkit-scrollbar,.simplebar-hide-scrollbar::-webkit-scrollbar{display:none;width:0;height:0}.simplebar-content:after,.simplebar-content:before{content:' ';display:table}.simplebar-placeholder{max-height:100%;max-width:100%;width:100%;pointer-events:none}.simplebar-height-auto-observer-wrapper{box-sizing:inherit!important;height:100%;width:100%;max-width:1px;position:relative;float:left;max-height:1px;overflow:hidden;z-index:-1;padding:0;margin:0;pointer-events:none;flex-grow:inherit;flex-shrink:0;flex-basis:0}.simplebar-height-auto-observer{box-sizing:inherit;display:block;opacity:0;position:absolute;top:0;left:0;height:1000%;width:1000%;min-height:1px;min-width:1px;overflow:hidden;pointer-events:none;z-index:-1}.simplebar-track{z-index:1;position:absolute;right:0;bottom:0;pointer-events:none;overflow:hidden}\[data-simplebar\].simplebar-dragging .simplebar-content{pointer-events:none;user-select:none;-webkit-user-select:none}\[data-simplebar\].simplebar-dragging .simplebar-track{pointer-events:all}.simplebar-scrollbar{position:absolute;left:0;right:0;min-height:10px}.simplebar-scrollbar:before{position:absolute;content:'';background:#000;border-radius:7px;left:2px;right:2px;opacity:0;transition:opacity .2s linear}.simplebar-scrollbar.simplebar-visible:before{opacity:.5;transition:opacity 0s linear}.simplebar-track.simplebar-vertical{top:0;width:11px}.simplebar-track.simplebar-vertical .simplebar-scrollbar:before{top:2px;bottom:2px}.simplebar-track.simplebar-horizontal{left:0;height:11px}.simplebar-track.simplebar-horizontal .simplebar-scrollbar:before{height:100%;left:2px;right:2px}.simplebar-track.simplebar-horizontal .simplebar-scrollbar{right:auto;left:0;top:2px;height:7px;min-height:0;min-width:10px;width:auto}\[data-simplebar-direction=rtl\] .simplebar-track.simplebar-vertical{right:auto;left:0}.hs-dummy-scrollbar-size{direction:rtl;position:fixed;opacity:0;visibility:hidden;height:500px;width:500px;overflow-y:hidden;overflow-x:scroll}.simplebar-hide-scrollbar{position:fixed;left:0;visibility:hidden;overflow-y:scroll;scrollbar-width:none;-ms-overflow-style:none} /\*\* \* One Dark theme for prism.js \* Based on Atom's One Dark theme: https://github.com/atom/atom/tree/master/packages/one-dark-syntax \*/ /\*\* \* One Dark colours (accurate as of commit 8ae45ca on 6 Sep 2018) \* From colors.less \* --mono-1: hsl(220, 14%, 71%); \* --mono-2: hsl(220, 9%, 55%); \* --mono-3: hsl(220, 10%, 40%); \* --hue-1: hsl(187, 47%, 55%); \* --hue-2: hsl(207, 82%, 66%); \* --hue-3: hsl(286, 60%, 67%); \* --hue-4: hsl(95, 38%, 62%); \* --hue-5: hsl(355, 65%, 65%); \* --hue-5-2: hsl(5, 48%, 51%); \* --hue-6: hsl(29, 54%, 61%); \* --hue-6-2: hsl(39, 67%, 69%); \* --syntax-fg: hsl(220, 14%, 71%); \* --syntax-bg: hsl(220, 13%, 18%); \* --syntax-gutter: hsl(220, 14%, 45%); \* --syntax-guide: hsla(220, 14%, 71%, 0.15); \* --syntax-accent: hsl(220, 100%, 66%); \* From syntax-variables.less \* --syntax-selection-color: hsl(220, 13%, 28%); \* --syntax-gutter-background-color-selected: hsl(220, 13%, 26%); \* --syntax-cursor-line: hsla(220, 100%, 80%, 0.04); \*/ code\[class\*="language-"\], pre\[class\*="language-"\] { background: #282c34; color: #abb2bf; text-shadow: 0 1px rgba(0, 0, 0, 0.3); font-family: "Fira Code", "Fira Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.5; tab-size: 2; -webkit-hyphens: none; hyphens: none; } /\* Selection \*/ code\[class\*="language-"\]::selection, code\[class\*="language-"\] \*::selection, pre\[class\*="language-"\] \*::selection { background: #3e4451; color: inherit; text-shadow: none; } /\* Code blocks \*/ pre\[class\*="language-"\] { padding: 1em; margin: 0.5em 0; overflow: auto; border-radius: 0.3em; } /\* Inline code \*/ :not(pre) > code\[class\*="language-"\] { padding: 0.2em 0.3em; border-radius: 0.3em; white-space: normal; } /\* Print \*/ @media print { code\[class\*="language-"\], pre\[class\*="language-"\] { text-shadow: none; } } .token.comment, .token.prolog, .token.cdata { color: #5c6370; } .token.doctype, .token.punctuation, .token.entity { color: #abb2bf; } .token.attr-name, .token.class-name, .token.constant, .token.number, .token.atrule { color: #d19a66; } .token.keyword, .token.boolean { color: #c678dd; } .token.property, .token.tag, .token.symbol, .token.deleted, .token.important { color: #e06c75; } .token.selector, .token.string, .token.char, .token.builtin, .token.inserted, .token.regex, .token.attr-value, .token.attr-value > .token.punctuation { color: #98c379; } .token.variable, .token.operator, .token.function { color: #61afef; } .token.url { color: #56b6c2; } /\* HTML overrides \*/ .token.attr-value > .token.punctuation.attr-equals, .token.special-attr > .token.attr-value > .token.value.css { color: #abb2bf; } /\* CSS overrides \*/ .language-css .token.selector { color: #e06c75; } .language-css .token.property { color: #abb2bf; } .language-css .token.function, .language-css .token.url > .token.function { color: #56b6c2; } .language-css .token.url > .token.string.url { color: #98c379; } .language-css .token.important, .language-css .token.atrule .token.rule { color: #c678dd; } /\* JS overrides \*/ .language-javascript .token.operator { color: #c678dd; } .language-javascript .token.template-string > .token.interpolation > .token.interpolation-punctuation.punctuation { color: #be5046; } /\* JSON overrides \*/ .language-json .token.operator { color: #abb2bf; } .language-json .token.null.keyword { color: #d19a66; } /\* MD overrides \*/ .language-markdown .token.url, .language-markdown .token.url > .token.operator, .language-markdown .token.url-reference.url > .token.string { color: #abb2bf; } .language-markdown .token.url > .token.content { color: #61afef; } .language-markdown .token.url > .token.url, .language-markdown .token.url-reference.url { color: #56b6c2; } .language-markdown .token.blockquote.punctuation, .language-markdown .token.hr.punctuation { color: #5c6370; font-style: italic; } .language-markdown .token.code-snippet { color: #98c379; } .language-markdown .token.bold .token.content { color: #d19a66; } .language-markdown .token.italic .token.content { color: #c678dd; } .language-markdown .token.strike .token.content, .language-markdown .token.strike .token.punctuation, .language-markdown .token.list.punctuation, .language-markdown .token.title.important > .token.punctuation { color: #e06c75; } /\* General \*/ .token.bold { font-weight: bold; } .token.comment, .token.italic { font-style: italic; } .token.entity { cursor: help; } .token.namespace { opacity: 0.8; } /\* Plugin overrides \*/ /\* Selectors should have higher specificity than those in the plugins' default stylesheets \*/ /\* Show Invisibles plugin overrides \*/ .token.token.tab:not(:empty):before, .token.token.cr:before, .token.token.lf:before, .token.token.space:before { color: rgba(171, 178, 191, 0.15); text-shadow: none; } /\* Toolbar plugin overrides \*/ /\* Space out all buttons and move them away from the right edge of the code block \*/ div.code-toolbar > .toolbar.toolbar > .toolbar-item { margin-right: 0.4em; } /\* Styling the buttons \*/ div.code-toolbar > .toolbar.toolbar > .toolbar-item > button, div.code-toolbar > .toolbar.toolbar > .toolbar-item > a, div.code-toolbar > .toolbar.toolbar > .toolbar-item > span { background: #3a3f4b; color: #828997; padding: 0.1em 0.4em; border-radius: 0.3em; } div.code-toolbar > .toolbar.toolbar > .toolbar-item > button:hover, div.code-toolbar > .toolbar.toolbar > .toolbar-item > button:focus, div.code-toolbar > .toolbar.toolbar > .toolbar-item > a:hover, div.code-toolbar > .toolbar.toolbar > .toolbar-item > a:focus, div.code-toolbar > .toolbar.toolbar > .toolbar-item > span:hover, div.code-toolbar > .toolbar.toolbar > .toolbar-item > span:focus { background: #3e4451; color: #abb2bf; } /\* Line Highlight plugin overrides \*/ /\* The highlighted line itself \*/ .line-highlight.line-highlight { background: rgba(153, 187, 255, 0.04); } /\* Default line numbers in Line Highlight plugin \*/ .line-highlight.line-highlight:before, .line-highlight.line-highlight\[data-end\]:after { background: #3a3f4b; color: #abb2bf; padding: 0.1em 0.6em; border-radius: 0.3em; box-shadow: 0 2px 0 0 rgba(0, 0, 0, 0.2); /\* same as Toolbar plugin default \*/ } /\* Hovering over a linkable line number (in the gutter area) \*/ /\* Requires Line Numbers plugin as well \*/ pre\[id\].linkable-line-numbers.linkable-line-numbers span.line-numbers-rows > span:hover:before { background-color: rgba(153, 187, 255, 0.04); } /\* Line Numbers and Command Line plugins overrides \*/ /\* Line separating gutter from coding area \*/ .line-numbers.line-numbers .line-numbers-rows, .command-line .command-line-prompt { border-right-color: rgba(171, 178, 191, 0.15); } /\* Stuff in the gutter \*/ .line-numbers .line-numbers-rows > span:before, .command-line .command-line-prompt > span:before { color: #636d83; } /\* Match Braces plugin overrides \*/ /\* Note: Outline colour is inherited from the braces \*/ .rainbow-braces .token.token.punctuation.brace-level-1, .rainbow-braces .token.token.punctuation.brace-level-5, .rainbow-braces .token.token.punctuation.brace-level-9 { color: #e06c75; } .rainbow-braces .token.token.punctuation.brace-level-2, .rainbow-braces .token.token.punctuation.brace-level-6, .rainbow-braces .token.token.punctuation.brace-level-10 { color: #98c379; } .rainbow-braces .token.token.punctuation.brace-level-3, .rainbow-braces .token.token.punctuation.brace-level-7, .rainbow-braces .token.token.punctuation.brace-level-11 { color: #61afef; } .rainbow-braces .token.token.punctuation.brace-level-4, .rainbow-braces .token.token.punctuation.brace-level-8, .rainbow-braces .token.token.punctuation.brace-level-12 { color: #c678dd; } /\* Diff Highlight plugin overrides \*/ /\* Taken from https://github.com/atom/github/blob/master/styles/variables.less \*/ pre.diff-highlight > code .token.token.deleted:not(.prefix), pre > code.diff-highlight .token.token.deleted:not(.prefix) { background-color: rgba(255, 82, 102, 0.15); } pre.diff-highlight > code .token.token.deleted:not(.prefix)::selection, pre.diff-highlight > code .token.token.deleted:not(.prefix) \*::selection, pre > code.diff-highlight .token.token.deleted:not(.prefix)::selection, pre > code.diff-highlight .token.token.deleted:not(.prefix) \*::selection { background-color: rgba(251, 86, 105, 0.25); } pre.diff-highlight > code .token.token.inserted:not(.prefix), pre > code.diff-highlight .token.token.inserted:not(.prefix) { background-color: rgba(26, 255, 91, 0.15); } pre.diff-highlight > code .token.token.inserted:not(.prefix)::selection, pre.diff-highlight > code .token.token.inserted:not(.prefix) \*::selection, pre > code.diff-highlight .token.token.inserted:not(.prefix)::selection, pre > code.diff-highlight .token.token.inserted:not(.prefix) \*::selection { background-color: rgba(56, 224, 98, 0.25); } /\* Previewers plugin overrides \*/ /\* Based on https://github.com/atom-community/atom-ide-datatip/blob/master/styles/atom-ide-datatips.less and https://github.com/atom/atom/blob/master/packages/one-dark-ui \*/ /\* Border around popup \*/ .prism-previewer.prism-previewer:before, .prism-previewer-gradient.prism-previewer-gradient div { border-color: #262931; } /\* Angle and time should remain as circles and are hence not included \*/ .prism-previewer-color.prism-previewer-color:before, .prism-previewer-gradient.prism-previewer-gradient div, .prism-previewer-easing.prism-previewer-easing:before { border-radius: 0.3em; } /\* Triangles pointing to the code \*/ .prism-previewer.prism-previewer:after { border-top-color: #262931; } .prism-previewer-flipped.prism-previewer-flipped.after { border-bottom-color: #262931; } /\* Background colour within the popup \*/ .prism-previewer-angle.prism-previewer-angle:before, .prism-previewer-time.prism-previewer-time:before, .prism-previewer-easing.prism-previewer-easing { background: #31363f; } /\* For angle, this is the positive area (eg. 90deg will display one quadrant in this colour) \*/ /\* For time, this is the alternate colour \*/ .prism-previewer-angle.prism-previewer-angle circle, .prism-previewer-time.prism-previewer-time circle { stroke: #abb2bf; stroke-opacity: 1; } /\* Stroke colours of the handle, direction point, and vector itself \*/ .prism-previewer-easing.prism-previewer-easing circle, .prism-previewer-easing.prism-previewer-easing path, .prism-previewer-easing.prism-previewer-easing line { stroke: #abb2bf; } /\* Fill colour of the handle \*/ .prism-previewer-easing.prism-previewer-easing circle { fill: transparent; } @charset "UTF-8"; @font-face { font-family: TTNorms; src: url(/static/media/TT\_Norms\_Pro\_Medium.2357aa49.woff2) format("woff2"), url(/static/media/TT\_Norms\_Pro\_Medium.9bebb1be.woff) format("woff"), url(/static/media/TT\_Norms\_Pro\_Medium.80a8a46c.eot) format("embedded-opentype"), url(/static/media/TT\_Norms\_Pro\_Medium.46b0321f.otf) format("opentype"), url(/static/media/TT\_Norms\_Pro\_Medium.4643446e.ttf) format("truetype"); font-weight: 500; font-style: normal; } @font-face { font-family: TTNorms; src: url(/static/media/TT\_Norms\_Pro\_Regular.2afefe1b.woff2) format("woff2"), url(/static/media/TT\_Norms\_Pro\_Regular.d71bcb57.woff) format("woff"), url(/static/media/TT\_Norms\_Pro\_Regular.0aca18c1.eot) format("embedded-opentype"), url(/static/media/TT\_Norms\_Pro\_Regular.e9f285aa.otf) format("opentype"), url(/static/media/TT\_Norms\_Pro\_Regular.88769ad2.ttf) format("truetype"); font-weight: 400; } html { font-family: TTNorms, Verdana, Geneva, sans-serif; font-size: 16px; font-weight: 400; line-height: 21px; color: #141E2D; } body, h1, h2, h3, h4, h5, p, span, a, ul, div, button { margin: 0; padding: 0; list-style: none; } input:focus { outline: none; } #root { display: flex; flex-direction: column; height: 100%; width: 100%; box-sizing: border-box; position: relative; min-height: 100vh; } button { text-decoration: none; background-color: unset; border: none; cursor: pointer; font-size: 14px; font-weight: 500; line-height: 17px; } .link, a { color: #3393FF; text-decoration-skip-ink: none; } .link:hover, a:hover { color: #2184F8; } .link:active, a:active { color: #1275EF; } .fw500 { font-weight: 500; } .header { position: relative; width: 100%; height: 60px; background-color: #141E2D; color: #FFFFFF; display: flex; justify-content: center; box-sizing: border-box; } .header\_\_container { display: flex; flex-direction: row; justify-content: space-between; width: 100%; max-width: 1420px; align-items: center; margin: 0 40px; transition: .4s; } .header\_\_logo { position: relative; text-decoration: none; } .header\_\_logo\_block { position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 160px; height: 20px; } .header\_\_logo\_title { margin-left: 176px; font-size: 24px; font-weight: 500; line-height: 31px; letter-spacing: -0.24px; text-decoration: none; color: #FFFFFF; } .header\_\_logo:hover { opacity: 0.9; } .header\_\_link { position: relative; padding-right: 21px; font-size: 24px; font-weight: 500; line-height: 31px; letter-spacing: -0.24px; color: #3393FF; text-decoration: none; } .header\_\_link:hover .header\_\_link\_icon path { stroke: #2184F8; } .header\_\_link:active .header\_\_link\_icon path { stroke: #1275EF; } .header\_\_link\_icon { position: absolute; top: 50%; transform: translateY(-50%); right: 0; width: 13px; height: 13px; } @media (max-width: 959px) { .header\_\_link { padding-right: 11px; font-size: 14px; font-weight: 500; line-height: 20px; } .header\_\_link\_icon { width: 9px; height: 9px; } } @media (max-width: 799px) { .header\_\_container { margin: 0 20px; transition: .4s; } .header\_\_logo\_block { width: 42px; } .header\_\_logo\_text { display: none; } .header\_\_logo\_title { margin-left: 58px; } } .footer { position: relative; color: #FFFFFF; background-color: #141E2D; } .footer\_\_container { box-sizing: content-box; position: relative; z-index: 1; margin: 0 auto; padding: 40px 20px 32px; max-width: 1420px; display: grid; grid-gap: 0 20px; gap: 0 20px; grid-template-areas: "partner" "nav" "app" "docs" "input" "social" "info"; } .footer\_\_partner { grid-area: partner; } .footer\_\_nav { margin-top: 32px; display: flex; flex-direction: column; grid-area: nav; } .footer .footer\_\_nav .nav-link-column:not(:first-child) { margin-top: 24px; } .footer\_\_input { margin-top: 32px; grid-area: input; } .footer\_\_app { margin-top: 24px; grid-area: app; } .footer\_\_docs { margin-top: 24px; grid-area: docs; } .footer\_\_social { margin-top: 32px; grid-area: social; } .footer\_\_social .social-links { margin-top: 16px; } .footer\_\_info { margin-top: 32px; grid-area: info; } @media screen and (min-width: 800px) { .footer\_\_container { padding: 40px 40px 32px; grid-template-columns: repeat(12, 1fr); grid-template-rows: 200px 74px repeat(3, auto); grid-template-areas: "partner partner partner partner partner partner nav nav nav nav nav nav" "input input input input input input nav nav nav nav nav nav" "social social social social social social nav nav nav nav nav nav" ". . . . . . app app app app app app" ". . . . . . docs docs docs docs docs docs" "info info info info info info info info info info info info"; } .footer\_\_nav { margin: 0; } .footer\_\_input { margin-top: 42px; max-width: 330px; } } @media screen and (min-width: 960px) { .footer\_\_container { grid-template-areas: "partner partner partner partner partner nav nav nav nav nav nav nav" "input input input input input nav nav nav nav nav nav nav" "social social social social social nav nav nav nav nav nav nav" ". . . . . app app app app app app app" ". . . . . docs docs docs docs docs docs docs" "info info info info info info info info info info info info"; } } @media screen and (min-width: 1260px) { .footer\_\_container { grid-template-columns: repeat(24, 1fr); grid-template-rows: unset; grid-template-areas: "partner partner partner partner partner partner partner .. nav nav nav nav nav nav nav nav nav nav nav nav nav nav nav nav" "input input input input input input input .. app app app app app app docs docs docs docs docs docs docs docs . ." "social social social social social social social .. info info info info info info info info info info info info info info info info"; } .footer\_\_nav { display: grid; grid-template-columns: 4fr 5fr 3fr 4fr; grid-gap: 20px; gap: 20px; grid-template-areas: "a b c d" "a b c e"; } .footer\_\_nav .nav-link-column:nth-child(1) { grid-area: a; } .footer\_\_nav .nav-link-column:nth-child(2) { grid-area: b; } .footer\_\_nav .nav-link-column:nth-child(3) { grid-area: c; } .footer\_\_nav .nav-link-column:nth-child(4) { grid-area: d; } .footer\_\_nav .nav-link-column:nth-child(5) { grid-area: e; } .footer .footer\_\_nav .nav-link-column\_\_list { flex-direction: column; grid-gap: 4px; gap: 4px; } .footer .footer\_\_nav .nav-link-column:not(:first-child) { margin-top: 0; } .footer\_\_app { margin-top: 42px; } .footer\_\_docs { margin-top: 72px; } .footer\_\_info, .footer\_\_social { margin-top: 32px; } } @media screen and (min-width: 1600px) { .footer\_\_container { grid-template-areas: "partner partner partner partner partner partner .. nav nav nav nav nav nav nav nav nav nav nav nav nav nav nav nav nav" "input input input input input input .. app app app app app docs docs docs docs docs docs docs docs . . . ." "social social social social social social .. info info info info info info info info info info info info info info info info info"; } .footer\_\_nav { grid-template-columns: 3fr 5fr repeat(3, 3fr); grid-template-areas: unset; } .footer\_\_nav .nav-link-column { grid-area: unset !important; } } .become-partner { box-sizing: border-box; } @media screen and (min-width: 800px) { .become-partner { padding: 20px 20px 20px 48px; max-width: 330px; background: url("//s.sweb.ru/img/footer\_left.svg") left/contain no-repeat; } } .become-partner\_\_title { font-size: 16px; font-weight: 500; line-height: 21px; margin: 0; } .become-partner\_\_list-title { font-size: 14px; font-weight: 400; line-height: 20px; margin: 8px 0 0; } .become-partner\_\_list-items { padding-left: 10px; } .become-partner\_\_list-item { font-size: 14px; font-weight: 400; line-height: 20px; position: relative; } .become-partner\_\_list-item::before { content: ""; position: absolute; top: 7px; right: calc(100% + 5px); width: 4px; height: 4px; background-color: #FFFFFF; border-radius: 50%; } .become-partner\_\_button { font-size: 14px; font-weight: 500; line-height: 20px; margin-top: 16px; padding: 8px 20px 6px; width: -moz-fit-content; width: fit-content; display: block; line-height: 17px; text-decoration: none; color: #FFFFFF; background-color: #3393FF; border-radius: 5px; transition: background-color 0.3s ease; } .become-partner\_\_button:hover { background-color: #2184F8; } .nav-link-column\_\_title { font-size: 16px; font-weight: 500; line-height: 21px; } .nav-link-column\_\_list { margin-top: 8px; display: flex; flex-wrap: wrap; grid-gap: 8px 16px; gap: 8px 16px; } @media screen and (min-width: 1260px) { .nav-link-column\_\_list { flex-direction: column; grid-gap: 4px; gap: 4px; } } .nav-link-column\_\_list-item a { font-size: 14px; font-weight: 400; line-height: 20px; display: block; width: 100%; color: #FFFFFF; text-decoration: underline; text-decoration-color: #37404c; text-underline-offset: 3px; transition: text-decoration-color 0.3s ease; } .nav-link-column\_\_list-item a:hover { text-decoration-color: #FFFFFF; } .nav-link-column\_\_list-item\_alternate a { color: #3393FF; text-decoration: none; } .nav-link-column\_\_list-item\_alternate a::after { content: ""; margin-left: 2px; width: 10px; height: 10px; display: inline-block; background: url(/static/media/link\_arrow\_right.2145ae93.svg) center/contain no-repeat; } .footer-form-search { box-sizing: border-box; padding-right: 8px; width: 100%; display: flex; align-items: center; background-color: #FFFFFF; border-radius: 5px; } .footer-form-search .footer-form-search\_\_input { font-size: 14px; font-weight: 400; line-height: 20px; padding: 6px 18px; min-height: unset; flex-grow: 1; color: #71839E; border: none; } .footer-form-search .footer-form-search\_\_submit { padding: 0; width: 16px; height: 16px; display: block; flex-shrink: 0; background: url("https://s.sweb.ru/img/icons/icon\_search.svg") center/contain no-repeat; border: none; cursor: pointer; } .download-app\_\_title { font-size: 16px; font-weight: 500; line-height: 21px; } .download-app\_\_links { margin-top: 8px; display: flex; flex-direction: row; grid-gap: 16px; gap: 16px; } .download-app\_\_link { height: 40px; } .download-app\_\_link a { display: block; } .docs-links { display: grid; grid-gap: 8px 20px; gap: 8px 20px; } @media screen and (min-width: 560px) and (max-width: 799px), (min-width: 960px) { .docs-links { grid-template-columns: repeat(8, 1fr); } } .docs-links .docs-links\_\_link { font-size: 10px; font-weight: 400; line-height: 14px; text-decoration: unset; } @media screen and (min-width: 560px) and (max-width: 799px), (min-width: 960px) { .docs-links .docs-links\_\_link { grid-column: span 5; } .docs-links .docs-links\_\_link:nth-child(even) { grid-column: span 3; } } @media screen and (min-width: 1600px) { .docs-links .docs-links\_\_link { grid-column: span 4; } } .phones-block\_\_item:not(:last-child) { margin-bottom: 4px; } .phones-block\_\_phone { text-decoration: none; color: #FFFFFF; } .phones-block\_\_location { color: #8997AC; } .social-links\_\_items { display: flex; grid-gap: 20px; gap: 20px; } .info-block { display: flex; flex-direction: column; grid-gap: 8px; gap: 8px; } .info-block\_\_text { font-size: 10px; font-weight: 400; line-height: 14px; margin: 0; color: #8997AC; } .info-block\_\_text a { text-decoration: none; } .nav { display: flex; flex-direction: column; width: 290px; height: max-content; position: sticky; top: 0; z-index: 20; } .nav\_\_tablet { height: 100%; width: 100%; box-sizing: border-box; position: relative; height: max-content; display: none; flex-direction: row; align-items: center; padding: 10px 20px 9px; background-color: #F5F8FB; cursor: pointer; width: 100%; } .nav\_\_tablet\_container { height: 100%; width: 100%; box-sizing: border-box; position: relative; margin-left: 12px; } .nav\_\_tablet\_title { font-size: 16px; font-weight: 500; line-height: 21px; } .nav\_\_tablet\_subtitle { white-space: nowrap; } .nav\_\_container { width: 100%; box-sizing: border-box; display: flex; flex-direction: column; padding: 20px 0; height: 100%; } .nav\_\_link { position: relative; height: min-content; width: 100%; display: flex; flex-direction: column; } .nav\_\_link:after { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background-color: #E6EFF8; } .nav\_\_link\_title { position: relative; display: inline-block; cursor: pointer; padding: 5.5px 0 5.5px 12px; text-decoration: none; color: #141E2D; font-size: 16px; font-weight: 500; line-height: 21px; } .nav\_\_link\_title + ul { overflow: hidden; height: 0; } .nav\_\_link\_title:hover:after { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background-color: #E6EFF8; background-color: #3393FF; opacity: 0.4; z-index: 1; } .nav\_\_link\_title.active:after { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background-color: #E6EFF8; background-color: #3393FF; z-index: 1; } .nav\_\_link\_title.active + .nav\_\_category { height: 100%; margin-top: 12px; margin-bottom: 12px; } .nav\_\_category { position: relative; width: 100%; margin-left: 12px; } .nav\_\_category\_link { display: inline-block; text-decoration: none; color: #141E2D; padding: 2.5px 0 2.5px 12px; cursor: pointer; max-width: 260px; } @media (max-width: 799px) { .nav\_\_category\_link { max-width: unset; } } .nav\_\_category\_link-method.active { font-size: 14px; font-weight: 500; line-height: 20px; color: #3393FF; } .nav\_\_category\_link.active:after { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background-color: #E6EFF8; background-color: #3393FF; z-index: 1; } .nav\_\_category\_link.active + .nav\_\_category.active { height: 100%; margin: 12px 0 12px 12px; } .nav\_\_category\_link:hover:after { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background-color: #E6EFF8; background-color: #3393FF; opacity: 0.4; z-index: 1; } .nav\_\_category\_link + ul { overflow: hidden; height: 0; } @media (max-width: 799px) { .nav { position: fixed; top: 60px; height: min-content; width: 100%; } .nav.open { height: 100%; } .nav.fixed { top: 0; } .nav\_\_tablet { display: flex; } .nav\_\_container { height: 0; background-color: #F5F8FB; z-index: 15; visibility: hidden; opacity: 0; overflow: hidden; padding: 0 20px; } .nav\_\_container.open { height: 100%; visibility: visible; opacity: 1; transition: all 0.3s ease; border-top: 1px solid #E6EFF8; padding: 20px; } } .content { height: 100%; width: 100%; box-sizing: border-box; position: relative; display: grid; grid-template-columns: repeat(12, 1fr); grid-column-gap: 20px; padding: 20px 0 0; } .content\_block { display: flex; flex-direction: column; } .content\_\_container { height: 100%; width: 100%; box-sizing: border-box; position: relative; display: grid; grid-template-columns: repeat(12, 1fr); grid-column-gap: 20px; } .content\_\_title { height: 100%; width: 100%; box-sizing: border-box; position: relative; display: flex; flex-direction: row; align-items: flex-end; } .content\_\_title\_h1 { font-size: 28px; font-weight: 500; line-height: 36px; letter-spacing: -0.28px; } .content\_\_title\_h2 { font-size: 24px; font-weight: 500; line-height: 31px; letter-spacing: -0.24px; } .content\_\_title\_description { font-size: 14px; font-weight: 400; line-height: 20px; color: #71839E; text-transform: lowercase; margin-left: 12px; margin-bottom: 3px; } .content\_\_title\_main { grid-column: 1/span 11; } .content\_\_server { display: grid; grid-column: 1/span 11; grid-template-columns: 5fr 6fr; grid-gap: 16px 20px; grid-template-rows: min-content; margin-top: 16px; padding-bottom: 32px; border-bottom: 1px solid #E6EFF8; } .content\_\_server\_methods { height: 100%; width: 100%; box-sizing: border-box; position: relative; display: flex; flex-direction: column; } .content\_\_server\_method { width: min-content; margin-left: 10px; text-decoration: underline; text-decoration-skip-ink: none; height: 21px; cursor: pointer; position: relative; margin-bottom: 2px; } .content\_\_server\_method:last-of-type { margin-bottom: 0; } .content\_\_server\_method:before { content: "•"; position: absolute; width: 10px; height: 19px; top: 0; left: -10px; } .content\_\_method { display: grid; grid-column: 1/span 11; grid-template-columns: 1fr; grid-template-rows: min-content; grid-gap: 24px; margin-top: 32px; padding-bottom: 32px; border-bottom: 1px solid #E6EFF8; } .content\_\_method\_instruction { margin-top: 16px; } .content\_\_method:last-of-type { border-bottom: none; } .content\_\_method\_table { padding: 5px 8px; height: min-content; border-bottom: 1px solid #E6EFF8; } .content\_\_method\_table-container { display: flex; flex-direction: column; overflow: auto; } .content\_\_method\_table-item { display: grid; grid-template-columns: max-content max-content 6fr; grid-template-rows: auto; grid-gap: 20px; padding: 5px 0; } .content\_\_method\_table-item .content\_\_method\_table-text { width: min-content; } .content\_\_method\_table-item .content\_\_method\_table-text:first-of-type { margin-left: 8px; } .content\_\_method\_table-item .content\_\_method\_table-text:last-of-type { width: 100%; margin-right: 8px; } .content\_\_method\_table:hover { background-color: #F5F8FB; } .content\_\_method\_table:last-of-type { border-bottom: none; } .content\_\_method\_table-text { width: 100%; } .content\_\_method\_json { position: relative; background-color: #062436; padding: 20px 6px 20px 20px; border-radius: 4px; max-height: 320px; box-sizing: border-box; } .content\_\_method\_json-button { position: absolute; top: 25px; right: 20px; width: 16px; height: 16px; padding: 0; } .content\_\_method\_json-button:hover { opacity: 0.9; } .content\_\_method\_text { position: relative; background-color: #062436; padding: 20px; border-radius: 4px; } .content\_\_element\_container { display: flex; flex-direction: column; } .content\_\_element\_title { display: inline-block; font-size: 14px; font-weight: 400; line-height: 20px; color: #71839E; margin-bottom: 8px; } .content\_\_examples { margin-top: 16px; grid-column: 1/span 11; } .content\_\_examples\_file.prettyprint { background-color: #141E2D; color: unset; } .content\_\_instruction { display: grid; grid-template-columns: 1fr; grid-template-rows: min-content; grid-gap: 24px; } .content\_\_instruction\_container { display: flex; flex-direction: column; } .content\_\_instruction\_code.language-javascript { background-color: #062436; padding: 0 44px 0 0; margin: 0; border-radius: 4px; } .content\_\_instruction\_code.language-javascript code { font-family: monospace, Verdana, Geneva, sans-serif; white-space: pre-wrap; word-wrap: anywhere; background-color: unset; font-size: 14px; font-weight: 700; line-height: 25px; } .content\_\_instruction\_code.language-javascript code.simple { color: #F5F5F5; } .content\_\_instruction\_code.language-javascript code.simple span { color: #F5F5F5; } .content\_\_instruction\_code.language-javascript code.token\_api { color: #F5F5F5; } .content\_\_instruction\_code.language-javascript code.token\_api .operator, .content\_\_instruction\_code.language-javascript code.token\_api .property, .content\_\_instruction\_code.language-javascript code.token\_api .constant { color: #F5F5F5; } .content\_\_instruction\_code.language-javascript code.token\_api .string { color: #EDA987; } .react-json-view { padding: 0 44px 0 0; overflow: hidden; word-wrap: anywhere; font-size: 14px; font-weight: 700; line-height: 25px; } .simplebar-track { background-color: rgba(225, 225, 225, 0.2); border-radius: 18px; } .simplebar-track.simplebar-vertical { width: 4px; } .simplebar-scrollbar { background-color: rgba(225, 225, 225, 0.6); opacity: .6; width: 4px; border-radius: 18px; } @media (max-width: 959px) { .content\_\_title\_main { grid-column: 1/span 12; } .content\_\_method { grid-column: 1/span 12; } .content\_\_examples { grid-column: 1/span 12; } .content\_\_server { grid-column: 1/span 12; } } @media (max-width: 799px) { .content { padding: 60px 20px 0; } .content\_\_server { grid-template-rows: auto; grid-template-columns: 1fr; grid-gap: 16px; padding-right: 0; } .content\_\_element\_container { overflow: auto; } .content\_\_method { padding-right: 0; } .content\_\_title\_main { padding-right: 0; } } @media (max-width: 559px) { .content { grid-template-columns: repeat(6, 1fr); } .content\_\_container { grid-template-columns: repeat(6, 1fr); } .content\_\_title\_main { grid-column: 1/span 6; } .content\_\_method { grid-column: 1/span 6; } .content\_\_examples { grid-column: 1/span 6; } .content\_\_server { grid-column: 1/span 6; } } #loader { width: 66px; height: 66px; border-radius: 100%; position: relative; margin: 0; } #loader.loader-small { width: 18px; height: 18px; } #loader.loader-medium { width: 32px; height: 32px; } .loader--wrapper { width: 100%; display: flex; position: relative; align-items: center; padding-top: 100px; padding-bottom: 100px; } .loader--wrapper.loader-small { padding-top: 0; padding-bottom: 0; } .loader--wrapper.loader-medium { padding-top: 0; padding-bottom: 0; } #loader:before, #loader:after { content: ""; position: absolute; width: 100%; height: 100%; border-radius: 100%; border: 2px solid transparent; border-top-color: #0DEFAB; } #loader:before { z-index: 100; animation: spin 0.8s infinite cubic-bezier(1, 0.5, 0.5, 0.5); } #loader:after { border: 2px solid #E6EFF8; } @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } } .main-container { display: flex; flex-direction: row; justify-content: center; flex: 1 1; position: relative; box-sizing: border-box; width: 100%; } .main-container:before { content: ""; position: absolute; top: 0; left: 0; width: calc(((100vw - 1420px) / 2) + 290px); height: 100%; background-color: #F5F8FB; } .main-container\_\_wrapper { width: 100%; max-width: 1420px; display: grid; grid-template-columns: min-content 1fr; grid-gap: 20px; position: relative; box-sizing: border-box; margin: 0 40px; } .scroll-top-button { position: fixed; width: 60px; height: 60px; border-radius: 50%; right: calc((100vw - 1420px) / 2); bottom: 115px; z-index: 10; visibility: visible; opacity: 1; transition: .3s opacity; } .scroll-top-button:hover circle { opacity: 0.7; } .scroll-top-button.hide { visibility: hidden; opacity: 0; transition: .3s opacity; pointer-events: none; } .scroll-top-button.absolute { position: absolute; } @media only screen and (max-width: 1500px) { .main-container:before { width: 334px; min-width: 334px; } } @media only screen and (max-width: 1460px) { .scroll-top-button { right: 20px; } } @media (max-width: 799px) { .main-container { flex-direction: column; } .main-container\_\_wrapper { grid-template-columns: 1fr; margin: 0; } .main-container:before { display: none; } }

[

API Портал](/instructions)[sweb.ru](https://sweb.ru)

VPS / Управление VPS

*   [Инструкция](/instructions)
*   [Примеры использования API](/examples)
*   Виртуальный хостинг
    *   [Сайты](/vh/sites)
        indexgetSiteInfoaddeditdelchangeDomainSitegetBackEndsListchangeBackEnd
    *   [Базы данных](/vh/hosting)
        databaseGetListdatabaseMysqlChangePassdatabaseMysqlCreatedatabaseMysqlImportdatabaseMysqlMakeCopydatabaseMysqlAccessListdatabaseMysqlAccessCreatedatabaseMysqlAccessDeletedatabaseMysqlDeletedatabasePgsqlCreatedatabasePgsqlDeletedatabasePgsqlChangePassdatabaseEditCommentgetPmaUser
    *   [Бэкапы](/vh/backup)
        getListmakeAccountCopyrestoreFilesdownloadFilegetListFilesgetListMysqlreceiveFilesreceiveMysqlrestoreMysql
    *   [Почта](/vh/mail)
        getDomainsListgetMailboxesListgetMailQuotacreateMboxsendRequisitesToEmaildropMboxupdateAntispamStateupdateCommentgetAutoreplychangeAutoreplychangeMailboxSpfchangeDomainSpfgetForwardingEmailsListaddForwardingEmailremoveForwardingEmailisEnabledDeletingAfterForwardingchangeDeletingAfterForwardinggetDeliveryAddressesListgetDeliveryInfoaddDeliveryAddressdropDeliveryAddressgetMailsCollectorchangeMailsCollectorremoveMailsCollectorconfirmMailsCollectorEmailchangeSenderVerifychangeAutoDiscoverdeleteMailschangeMailboxPasswordgetWhitelistgetBlacklistaddToWhitelistaddToBlacklistdropFromWhitelistdropFromBlacklistenableDkimdisableDkim
    *   [SSL](/vh/ssl)
        indexgetOrderListdownloadeditAutoprolongremoveCertificategetProlongInfoprolongCertificateinstallLetsEncrypt
    *   [Тариф](/vh/tariff)
        indexserverInfo
    *   [Нагрузка](/vh/load)
        indexgetLoadTable
    *   [SSH](/vh/utils)
        sshOnsshOff
    *   [Квота](/vh/disk-usage)
        indexgetTasksInfostartTaskgetEmailchangeEmail
    *   [Crontab](/vh/cron)
        addTaskeditTaskremoveTaskgetTasks
    *   [DDG](/vh/ddg)
        indexcountAllDomainsenabledisableenableInfopriceWidgetgetPrice
*   VPS
    *   [Управление VPS](/vps)
        indexgetFirstOrderInfocreateEnablegetAvailableConfigcopycreateFirstcreaterenameisRunningremoveremoveFirstloadgetConstructorPlanIdchangePlanpowerOnpowerOffrebootgetCurrentActionreinstallOslogs
    *   [Бэкапы](/vps/backup)
        indexupdateIndexcreaterestoreattachdetachremovegetSettingssaveSettings
    *   [SSL](/vps/ssl)
        indexgetOrderListdownloadeditAutoprolongremoveCertificategetProlongInfoorderSubmit
    *   [Локальная сеть](/vps/ip)
        addLocalremoveLocal
    *   [IP-адреса](/vps/protected-ip)
        indexgetAllIpListgetOrderInfoaddProtectedremoveProtectedupdateProtectedmoveProtectedaddaddLocalremoveLocalremovemoveeditPtrgetPtr
    *   [DBaaS](/vps/dbaas)
        indexsetUpgradeAgreegetAvailableConfiggetConstructorPlanIdgetFirstOrderInforemoveFirstcreateInstanceeditInstanceremoveInstancedeleteDatabasevalidateUsers
    *   [Балансировщик](/vps/balancer)
        indexisCreateEnablegetAvailableConfigcreateeditremove
    *   [Облачные бэкапы](/vps/remote-backup)
        indexcreateeditCommentrestorerestoreIntoremove
    *   [Мониторинг](/vps/monitoring)
        enabledisablechangeplans
    *   [Мониторинг. Проверки](/vps/monitoring/checks)
        indexgetTypesgetIntervalsgetPortsgetKeywordModesgetInfogetFullCheckInfocreateeditactivateactivateListdeactivatedeactivateListremoveremoveListhistory
    *   [Мониторинг. Контакты](/vps/monitoring/contacts)
        indexgetAllContactsaddContacteditContactaddEmaileditEmailaddPhoneeditPhonedeleteContactdeleteContactsaddTelegramrequestTelegramVerifyCodeisVerifiededitTelegramverifyContact
*   Домены
    *   [Домены](/domains)
        indexgetSubdomainsgetDomainInforegAvailablegetAvailablePackagesregListregmovemoveListchangeProlongchangeProlongListremoveremoveListprolongprolongListpriceForTrasferpriceForRegistrationremoveSubdomaincreateSubdomainsetRedirectVhgetRedirectVh
    *   [Доменные бонусы](/domains/bonus)
        indexgetListbuy
    *   [Доменные персоны](/domains/persons)
        indexgetinfocreateFizIpcreateJur
    *   [DNS](/domains/dns)
        infoeditMxeditSrveditNSeditTxtgetFile
*   Партнерская программа
    *   [Партнерская программа](/partner-program)
        createOrderVhcheckLogincreateOrderVipcreateOrderVpsstandardPlansvipPlansvpsOsConfigstartPartnershipfillPartnerRequisitesgetTypesAdvertMaterialsgetAdvertMaterialsgetPartnerClientsListgetPartnerClientCardsavePartnerClientCommentgetPartnerClientLogEventsgetPartnerClientLogFinancesendWithdrawalOrdergetRequisitesWithdrawalgetStatisticgetLinkStatistics
    *   [Реферальные сайты](/referral-program)
        indexremoveReferralSiteconfirmReferralSiteaddReferralSite
*   Оплата и финансы
    *   [Оплата и финансы](/pay)
        indexisAutopaymentEnablegetPayRecommendationsgetRecommendationTotalCostgetUpcomingPaymentsVhchangeDefermentgetRemainsDategetRemainsDaysgetBalancegetActiveReserves

Vps
===

объект

описание

Объект VPS

применяемость

VPS

путь к объекту

POST https://api.sweb.ru/vps

требование к авторизации

да

список методов

*   index;
*   getFirstOrderInfo;
*   createEnable;
*   getAvailableConfig;
*   copy;
*   createFirst;
*   create;
*   rename;
*   isRunning;
*   remove;
*   removeFirst;
*   load;
*   getConstructorPlanId;
*   changePlan;
*   powerOn;
*   powerOff;
*   reboot;
*   getCurrentAction;
*   reinstallOs;
*   logs.

index
-----

метод

описание

Список VPS

возвращаемые значения в свойствах элементов массива

'billingId' string ID сервиса

'name' string Имя VPS

'plan\_id' int ID плана

'plan\_name' string Название палана

'parent\_plan\_id' int ID родительского плана

'plan\_price' int Стоимость

'cpu' int Число процессоров

'ram' string Количество памяти

'disk' string Размер диска

'blockUi' int Заблокирована

'active' int Активна

'uid' string Идентификатор машины

'os\_distribution' string Название ОС

'os\_distr\_id' int ID Дистрибутива

'category' string Категория

'ts\_create' string Дата создания

'mac' string MAC-адрес

'ip' string IP

'local\_ip' string локальный IP

'local\_mac' string локальный MAC

'local\_mask' string локальная маска подсети

'current\_action' string Текущая операция

'is\_running' int Запущена

'isp' array Информация о панели управления:

'license\_type' string Название панели

'ip' string IP

'active\_until' string Активна до даты

'price' float Стоимость

'link' string Ссылка на вход в панель

'is\_blocked' int Заблокирована

'creation\_time' string Дата создания

'ext\_ips' array Информация о доп. IP:

'is\_test' int Тестовый период

'is\_new' bool Новая услуга

'datacenter' string Дата-центр

'ordered\_ip\_count' int Количество адресов, заказанных на VPS

'protected\_ips'

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"index"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"720081569636118.LjJMsKaidf"

"result":\[

{

"billingId":

"inn\*\*\*\*\_vps\_4"

"name":

"inn\*\*\*\*\_vps\_4"

"plan\_id":

"4"

"plan\_name":

"KVM-10"

"parent\_plan\_id":

NULL

"plan\_price":

349

"cpu":

2

"ram":

"1024"

"disk":

"10 ГБ"

"blockUi":

1

"active":

0

"uid":

"a0a23dcee\*\*\*\*\*\*\*\*\*\*\*\*\*"

"os\_distribution":

"Ubuntu 22.04 LTS"

"os\_distr\_id":

102

"category":

"nvme"

"ts\_create":

"2023-06-26 15:38:20"

"mac":

"00:16:3e:77:a2:26"

"ip":

"77.222.43.225"

"local\_ip":

NULL

"local\_mac":

NULL

"local\_mask":

NULL

"current\_action":

""

"is\_running":

0

"isp":\[

{

"license\_type":

"LEMP"

"ip":

"77.222.43.225"

"active\_until":

""

"price":

0

"link":

""

"is\_blocked":

0

"creation\_time":

"10-15"

}

\]

"ext\_ips":\[\]

"is\_test":

0

"is\_new":

false

"datacenter":

"Москва"

"ordered\_ip\_count":

2

"protected\_ips":\[

"127.0.105.53"

\]

}

\]

}

getFirstOrderInfo
-----------------

метод

описание

Получение информации о первом заказе

возвращаемые значения в свойствах элементов массива

'plan' string Название плана

'os' string Название ОС

'panel' string Название ПУ

'cpu\_cores' string Количество процессоров

'ram' string Количество памяти

'volume\_disk' string Размер диска

'price\_per\_month' int Цена за месяц

'pay\_period' int Цена за период

'price\_for\_period\_with\_stock' int Цена за месяц со скидкой

'price\_per\_month\_with\_stock' int Цена за период со скидкой

'promocode' string|null Промо-код на скидку (не партнерский) введенный при регистрации

'clearAvailable' bool Доступна возможность очистки первого заказа

'plan\_is\_constructor' bool Флаг сконструированного тарифа

'ipCount' int Кол-во не защищенных IP в заказе

'protectedIps' int\[\] Массив ID тарифов защищенных IP для заказа (например, \[1, 3, 3\])

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getFirstOrderInfo"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"171633869878845.iBlzwvGSEL"

"result":\[

{

"jsonrpc":

"2.0"

"version":

"1.263.20250326113457"

"id":

"20250327104613.kmuG0Cu94B"

"result":{

"plan":

"CLOUD PROMO на год"

"os":

"Ubuntu 24.04 LTS"

"panel":

"Без ПО"

"cpu\_cores":

"1"

"ram":

"1024"

"volume\_disk":

"10 ГБ"

"price\_per\_month":

139

"pay\_period":

12

"price\_for\_period\_with\_stock":

1668

"price\_per\_month\_with\_stock":

139

"promocode":

NULL

"clearAvailable":

false

"plan\_is\_constructor":

false

"ipCount":

1

"protectedIps":\[

1

2

\]

}

}

\]

}

createEnable
------------

метод

описание

Проверка доступен ли заказ VPS

возвращаемое значение

1 - успешно, 0 - ошибка

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"createEnable"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"888990632800705.sNMzlIEKwE"

"result":

1

}

getAvailableConfig
------------------

метод

описание

Получение списка доступных дистрибутивов, ISP-лицензий, тарифных планов

возвращаемые значения в свойствах элементов массива

'vpsPlans' array Тарифные планы

Каждый тарифный план содержит массив значений:

'id' int id тарифного плана

'ts\_create' string дата и время создания в формате YYYY-MM-DD HH:MM:SS

'ts\_update' string дата и время обновления в формате YYYY-MM-DD HH:MM:SS

'billing\_id' string id услуги

'category\_id' string id категории тарифного плана

'name' string название тарифа

'price\_per\_month' int стоимость одного месяца при помесячной оплате

'parent\_plan\_id' int|null id родительского тарифного плана

'cpu\_cores' string кол-во ядер

'ram' string кол-во оперативной памяти

'disk\_type' string тип диска

'volume\_disk' string ёмкость диска

'units' string кол-во занимаемых юнитов

'is\_promo' string является ли промо-трифом (0 - не является)

'package\_duration' string длительность пакета в месяцах

'constructor' string относится ли тариф к категории Конструктор сайтов (N - не относится)

'year\_price\_per\_month' int стоимость одного месяца в годовом пакете

'category' string название категории тарифного плана

'datacenters' array массив из id дата-центров

'price\_per\_month\_promo' int стоимость месяца промо-версии тарифа при помесячной оплате

'year\_price\_per\_month\_promo' int стоимость месяца промо-версии тарифа в годовом пакете

'selectOs' array Операционные системы

Каждая ОС содержит массив значений:

'id' string id операционной системы

'name' string название ОС

'description' string более подробное название ОС

'order' string порядковый номер для сортировки в списке

'url' string|null ссылка на страницу с информацией об ОС

'full\_description' string|null полное подробное описание

'plan\_id' string id тарифного плана по умолчанию

'os\_distribution\_id' string id сборки

'panel\_type' array массив названий доступных панелей управления (empty - без ПУ)

'selectPanel' array Панели управления

Каждая панель управления содержит массив значений:

'id' string id панели управления

'name' string алиас названия

'description' string полное название

'order' string порядковый номер для сортировки в списке

'creation\_time' string|null диапазон времени(в минутах)

'url' string|null ссылка на страницу с информацией о панели управления

'full\_description' string|null полное подробне описание

'plan\_id' string id тарифного плана по умолчанию для данной панели

'os\_distribution\_id' string id сборки

'action' int действует ли акция на данную панель управления (0 - нет акции)

'price' int текущая стоимость панели управления в месяц с учетом активности акции (0 - бесплатно)

'old\_price' int базовая стоимость панели управления без акции

'osPanel' array Дистрибутивы (операционная система+панель). distributive передается в create

Каждый дистрибутив содержит массив значений:

'distributive' string id дистрибутива

'os' string id операционной системы

'panel' string id панели

'availablePlanIds' array массив из id тарифных планов доступных с этим дистрибутивом

'minRam' int минимальное кол-во ОЗУ (Гб)

'minStorage' int минимальный объем на диске

'datacenters' array Доступные дата-центры

Каждый дата-центр содержит массив значений:

'id' string id дата-центра

'name' string алиас названия (spb / msk)

'location' string название местоположения (Санкт-Петербург)

'site\_name' string название дата-центра для пользователей

'categories' array Категории тарифных планов

Каждая категория содержит массив значений:

'id' string id категории

'slug' string алиас категории

'name' string название категории для пользователей

'prior' string порядковый номер для сортировки в списке

'kit' array массив параметров для конфигуратора тарифов категории NVME:

'cpuCores' array параметры для установки кол-ва ядер:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении кол-ва ядер

'price' int стоимость одного ядра

'ram' array параметры для установки кол-ва ОЗУ:

'values' array массив из доступных объемов в Гб:

'price' int стоимость одного Гб

'volumeDisk' array параметры для установки объема жесткого диск:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении объема диска

'price' int стоимость одного Гб

'price\_backup' int стоимость одного Гб бэкапа

'categoryId' int id категории тарифного плана

'kit\_turbo' array массив параметров для конструктора тарифов категории Turbo:

'cpuCores' array параметры для установки кол-ва ядер:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении кол-ва ядер

'price' int стоимость одного ядра

'ram' array параметры для установки кол-ва ОЗУ:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема ОЗУ в Гб

'price' int стоимость одного Гб

'volumeDisk' array параметры для установки объема жесткого диска:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема жесткого диска в Гб

'price' int стоимость одного Гб

'price\_backup' int стоимость одного Гб бэкапа

'categoryId' int id категории тарифного плана

'kit\_hdd' array массив параметров для конструктора тарифов категории HDD:

'cpuCores' array параметры для установки кол-ва ядер:

'start' int минимальное значение

'end' int максимальное значение

'step' int размер шага при изменении кол-ва ядер

'price' int стоимость одного ядра

'ram' array параметры для установки кол-ва ОЗУ:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема ОЗУ в Гб

'price' int стоимость одного Гб

'volumeDisk' array параметры для установки объема жесткого диска:

'start' int минимальное значение в Гб

'end' int максимальное значение в Гб

'step' int размер шага при изменении объема жесткого диска в Гб

'price' int стоимость одного Гб

'categoryId' int id категории тарифного плана

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getAvailableConfig"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"795506945436770.AHWsEwMbad"

"result":{

"vpsPlans":\[

{

"id":

4

"ts\_create":

"2015-09-29 13:43:43"

"ts\_update":

"2021-09-22 11:48:03"

"billing\_id":

"597"

"category\_id":

"1"

"name":

"KVM-10"

"price\_per\_month":

349

"parent\_plan\_id":

NULL

"cpu\_cores":

"2"

"ram":

"1024"

"disk\_type":

"NVMe"

"volume\_disk":

"10 ГБ"

"units":

"1"

"is\_promo":

"0"

"package\_duration":

"1"

"constructor":

"N"

"year\_price\_per\_month":

299

"category":

"nvme"

"datacenters":\[

1

2

\]

"price\_per\_month\_promo":

239

"year\_price\_per\_month\_promo":

239

}

{

"id":

5

"ts\_create":

"2015-09-29 13:43:43"

"ts\_update":

"2022-03-18 09:16:03"

"billing\_id":

"598"

"category\_id":

"1"

"name":

"KVM-20"

"price\_per\_month":

649

"parent\_plan\_id":

NULL

"cpu\_cores":

"2"

"ram":

"2048"

"disk\_type":

"NVMe"

"volume\_disk":

"20 ГБ"

"units":

"2"

"is\_promo":

"0"

"package\_duration":

"1"

"constructor":

"N"

"year\_price\_per\_month":

549

"category":

"nvme"

"datacenters":\[

1

2

\]

"price\_per\_month\_promo":

439

"year\_price\_per\_month\_promo":

439

}

{

"id":

42

"ts\_create":

"2021-11-22 14:18:18"

"ts\_update":

NULL

"billing\_id":

"1606"

"category\_id":

"3"

"name":

"TURBO-160"

"price\_per\_month":

4099

"parent\_plan\_id":

NULL

"cpu\_cores":

"4"

"ram":

"8192"

"disk\_type":

"NVMe"

"volume\_disk":

"160 ГБ"

"units":

"16"

"is\_promo":

"0"

"package\_duration":

"1"

"constructor":

"N"

"year\_price\_per\_month":

3299

"category":

"turbo"

"datacenters":\[

1

2

\]

"price\_per\_month\_promo":

2639

"year\_price\_per\_month\_promo":

2639

}

\]

"selectOs":\[

{

"id":

"20"

"name":

"ubuntu-20-04"

"description":

"Ubuntu 20.04 LTS"

"order":

"1"

"url":

NULL

"full\_description":

NULL

"plan\_id":

"4"

"os\_distribution\_id":

"32"

"panel\_type":\[

"empty"

"isp"

"docker"

"nodejs"

"rocket"

"gitlab"

"hestia"

"nextcloud"

"fastpanel"

"minecraft"

\]

}

{

"id":

"13"

"name":

"debian-9"

"description":

"Debian 9"

"order":

"103"

"url":

NULL

"full\_description":

NULL

"plan\_id":

"4"

"os\_distribution\_id":

"22"

"panel\_type":\[

"empty"

"isp"

\]

}

{

"id":

"19"

"name":

"bitrix-auto-centos-7"

"description":

"BitrixVM 7"

"order":

"104"

"url":

"https://sweb.ru/vds/bitrix/"

"full\_description":

"Готовое решение для продуктов на 1С-Битрикс"

"plan\_id":

"6"

"os\_distribution\_id":

"30"

"panel\_type":\[

"empty"

\]

}

\]

"selectPanel":\[

{

"id":

"7"

"name":

"empty"

"description":

"Без ПО"

"order":

"0"

"creation\_time":

NULL

"url":

NULL

"full\_description":

NULL

"plan\_id":

"5"

"os\_distribution\_id":

"0"

"action":

0

"price":

0

"old\_price":

0

}

{

"id":

"4"

"name":

"vps\_isp6\_lite"

"description":

"ISPmanager 6 Lite"

"order":

"2"

"creation\_time":

"20-30"

"url":

"https://help.sweb.ru/entry/728/"

"full\_description":

"Популярная панель управления сервером, 10 сайтов"

"plan\_id":

"5"

"os\_distribution\_id":

"77"

"action":

0

"price":

300

"old\_price":

300

}

{

"id":

"9"

"name":

"nodejs"

"description":

"Node.js"

"order":

"8"

"creation\_time":

"10-15"

"url":

NULL

"full\_description":

"Серверная платформа для работы с JavaScript"

"plan\_id":

"5"

"os\_distribution\_id":

"62"

"action":

0

"price":

0

"old\_price":

0

}

{

"id":

"10"

"name":

"rocket"

"description":

"Rocket.Chat"

"order":

"9"

"creation\_time":

"10-15"

"url":

NULL

"full\_description":

"Корпоративный мессенджер с открытым исходным кодом"

"plan\_id":

"5"

"os\_distribution\_id":

"63"

"action":

0

"price":

0

"old\_price":

0

}

{

"id":

"11"

"name":

"gitlab"

"description":

"GitLab"

"order":

"10"

"creation\_time":

"15-30"

"url":

NULL

"full\_description":

"Система управления репозиториями программного кода для Git"

"plan\_id":

"6"

"os\_distribution\_id":

"64"

"action":

0

"price":

0

"old\_price":

0

}

{

"id":

"15"

"name":

"minecraft"

"description":

"Minecraft JE Server"

"order":

"11"

"creation\_time":

"10-15"

"url":

"https://sweb.ru/vds/minecraft/"

"full\_description":

"Сервер игры Minecraft Java Edition"

"plan\_id":

"6"

"os\_distribution\_id":

"89"

"action":

0

"price":

0

"old\_price":

0

}

\]

"osPanel":\[

{

"distributive":

"8"

"os":

"4"

"panel":

"7"

"availablePlanIds":\[

4

5

6

12

14

26

28

34

38

42

\]

"minRam":

0

"minStorage":

0

}

{

"distributive":

"89"

"os":

"20"

"panel":

"15"

"availablePlanIds":\[

5

6

12

14

26

28

34

38

42

\]

"minRam":

2

"minStorage":

0

}

\]

"datacenters":\[

{

"id":

"1"

"name":

"spb"

"location":

"Санкт-Петербург"

"site\_name":

"Дата-центр в СПБ"

}

{

"id":

"2"

"name":

"msk"

"location":

"Москва"

"site\_name":

"Дата-центр в Москве"

}

\]

"categories":\[

{

"id":

"1"

"slug":

"nvme"

"name":

"VPS/VDS на NVMe (быстрые)"

"prior":

"1"

}

{

"id":

"3"

"slug":

"turbo"

"name":

"VPS/VDS HighCPU (турбо)"

"prior":

"2"

}

{

"id":

"2"

"slug":

"hdd"

"name":

"VPS/VDS на HDD (большого объёма)"

"prior":

"3"

}

{

"id":

"4"

"slug":

"kit"

"name":

"Конфигуратор VPS/VDS"

"prior":

"4"

}

\]

"kit":{

"cpuCores":{

"start":

2

"end":

16

"step":

2

"price":

110

}

"ram":{

"values":\[

1

2

3

4

6

8

10

12

14

16

18

20

22

24

26

28

30

32

\]

"price":

115

}

"volumeDisk":{

"start":

10

"end":

320

"step":

10

"price":

15

"price\_backup":

1.5

}

"categoryId":

1

}

"kit\_turbo":{

"cpuCores":{

"start":

1

"end":

4

"step":

1

"price":

530

}

"ram":{

"start":

2

"end":

8

"step":

1

"price":

140

}

"volumeDisk":{

"start":

40

"end":

160

"step":

10

"price":

9

"price\_backup":

3

}

"categoryId":

3

}

"kit\_hdd":{

"cpuCores":{

"start":

1

"end":

2

"step":

1

"price":

530

}

"ram":{

"start":

2

"end":

4

"step":

1

"price":

160

}

"volumeDisk":{

"start":

500

"end":

1000

"step":

10

"price":

2

}

"categoryId":

2

}

}

}

copy
----

метод

описание

Клонирование VPS

возвращаемое значение

создание/клонирование VPS

параметры в запросе

billingId

string

идентификатор машины

vpsPlanId

integer

новый тарифный план

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"copy"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"vpsPlanId":

4

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"539485902873327.lePGrCwkRE"

"result":

"vhp\*\*\*\*\_vps\_2"

}

createFirst
-----------

метод

описание

Создание первого заказа с VPS

возвращаемое значение

создание/клонирование VPS

параметры в запросе

distributiveId

integer

ID Дистрибутива

vpsPlanId

integer

ID Тарифного плана

datacenter

integer

Датацентр

alias

string

Название VPS

sshKey

string

Публичный SSH-ключ

sshKeyName

string

Имя ключа

privateIp

boolean

Подключить к локальной сети

period

integer

Период оплаты (1 или 12 мес.)

startTestPeriod

boolean

Начать тестовый период

monitoringPlanId

integer

ID плана мониторинга

monitoringContactId

integer

ID контакта мониторинга

ipCount

integer

Кол-во заказанных вместе с VPS IP-адресов (для 1ого заказа: 0 или 1)

protectedIps

array

Массив ID тарифов защищенных IP для заказа (например, \[1, 3, 3\])

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"createFirst"

"params":{

"distributiveId":

32

"vpsPlanId":

4

"datacenter":

1

"period":

1

"startTestPeriod":

true

"ipCount":

1

"protectedIps":\[

1

2

3

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"207117702707782.xXEErhZiJx"

"result":

"vhp\*\*\*\*\_vps\_1"

}

create
------

метод

описание

Создание VPS

возвращаемое значение

создание/клонирование VPS

параметры в запросе

distributiveId

integer

ID Дистрибутива

vpsPlanId

integer

ID Тарифного плана

datacenter

integer

датацентр

alias

string

название VPS

sshKey

string

публичный SSH-ключ

sshKeyName

string

имя ключа

privateIp

boolean

подключить к локальной сети

monitoringPlanId

integer

ID плана мониторинга

monitoringContactId

integer

ID контакта мониторинга

remoteBackupId

integer

ID бэкапа

ipCount

integer

кол-во заказанных вместе с VPS IP-адресов

protectedIps

integer

массив ID тарифов защищенных IP для заказа (например, \[1, 3, 3\])

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"create"

"params":{

"distributiveId":

32

"vpsPlanId":

4

"datacenter":

1

"alias":

"hestiaVPS"

"sshKey":

"ssh-rsa ......."

"monitoringPlanId":

1

"monitoringContactId":

2642

"ipCount":

2

"protectedIps":\[

1

2

\]

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"921832275382655.QvWznXfvab"

"result":

"vhp\*\*\*\*\_vps\_2"

}

rename
------

метод

описание

Переименование VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

alias

string

название VPS

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"rename"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"alias":

"hestiaVPS"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"534460260727581.ktleXhvmed"

"result":

1

}

isRunning
---------

метод

описание

Запущена ли VPS в данный момент

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"isRunning"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"998654563950036.aIgqVlSLwG"

"result":

1

}

remove
------

метод

описание

Удаление VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"remove"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"669713065950971.vfsVDeDrel"

"result":

1

}

removeFirst
-----------

метод

описание

Удаление первого заказа.Доступно, если заказ ещё не был оплачен и услуга не стартовала

возвращаемое значение

1 - успешно, 0 - ошибка

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"removeFirst"

"params":{}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"503723158316028.itBMJqOzOz"

"result":

1

}

load
----

метод

описание

Загрузка - возвращает картинку в Base64

возвращаемые значения в свойствах элементов массива

'mimetype' string MIME-тип данных (image/png;base64)

'metadata' array мета-данные

'content' string содержимое в base64

параметры в запросе

billingId

string

идентификатор машины

type

string

тип нагрузки ('cpu', 'hdd\_ops', 'net')

from

string

дата начала

to

string

дата окончания

width

integer

ширина графика

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"load"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"type":

"hdd\_ops"

"from":

"08-03-2023"

"to":

"15-03-2023"

"width ":

640

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"734579342681177.QANhhrenec"

"result":{

"mimetype":

"image/png;base64"

"metadata":\[\]

"content":

"i9JBn6w8NgMEydOrVdu3ZAgMDExMT3333XUX+YarX65OTk53jdsaMGcXFxXI3yvMCAgJWrFjRtWtXadw+/vjjJ0+elLtRnqfVar/++uukpCRp3Pbo0WPt2rVyN8rzOI6rrKycPHmyc9zOmjWrtLRU7nZ5BgKwO6ZNmxYbG5uZmWk0Gs+dOxcREaHIlZ8NGzYcPXo0NTW1qqoqJydn/vz5kydPLioqkrtdHnb79u2UlJRFixbl5uZWVFTs2bNn7969NR8zU4zk5OROnTpJ4zYjIyMkJESRK+3r168/ceLE/v37q6qqsrOzX3zxxUmTJinmV7bTzZs3Z82atWTJEmnc7ty5c+fOnTUf11GMyZMnJyQkZGVlSePW399/9uzZcjfKQ+TLhOjFgoKCpFywY8eOpZRWVFSEhobK3SjPS0lJ2bp1K6V06dKlly9fppQOGzbs2LFjcrfLww4ePChdx4yMjLfeeotSunHjxrlz58rdLg8TRdHPz89kMlFKx40bRyktKSmJjIyUu12el5yc/Nlnn1FKFy5c+P3331NKhwwZ8vXXX8vcLE9LTU196qmnKKWnT59etWoVpXT9+vXz5s2Tu10eJgiCVqu1Wq2iKErjtqCgICYmRu52eQYCsDsee+yxhQsXFhQU2O32vLy8BQsWjBw5Uu5Ged4HH3yQlJT03XffWSwWnU63d+/eqKiowsJCudvlYTk5OVFRUQcOHNDr9Waz+eLFi3379t2yZYvc7fK8pKSkJUuWSOM2Nzd33rx5Tz75pNyN8rz33ntvyJAhV65csVgsVVVVn3/+eVRUVGlpqdzt8rCbN2+2adPm4MGD0rjNysrq06fPjh075G6X5w0YMGDZsmWFhYXSuH3ppZekg1YUAAHYHfn5+SkpKbGxsdI9iZkzZxYVFcndKM8TBGHFihXdunVz3ktT3jRC8uWXXz766KPh4eEBAQE9evRYs2aNKIpyN8rzcnNza+5d+N3vfldSUiJ3ozxPEITly5cnJCT4+/tHRkYOGzbs1KlTcjeqWRw5csS5d6Fnz57r1q2Tu0XN4vbt2869C+3bt3/hhRcU8+cUdkEDAADIAJuw7hvOglYYnAWtMDgLWklwFjTUhrOgFQZnQSsMzoJWEpwFDf8fnAWtMDgLWmFwFrSS4CxoqA1nQSsMzoJWEpwFrTA4Cxpqw1nQSoKzoBUGZ0ErDM6Chp/hTF0l8ZEzdQnGrbL4yLilOAsaajl69Ojzzz/vfPmb3/zm8OHDMranmZjN5v79+5eXl0svd+zYoch5oVarnT59+qFDh6SXxcXF3bt31+l08raqORw6dKjmFRw/fnx6erqM7Wkmer2+b9++0n1uQsiWLVvmzp0rb5Oag1arnTx5srQ/gxBSVFTUq1cvg8Egb6s8juO4ffv2zZkzx/nOqFGjlHMovbyPIXupxMTE69evC4KgUqkopZmZmf369ZO7UZ63bNmylStXUkqfeeaZ1NRUURTj4+Ozs7PlbpeHXbp0qW/fvpTSXbt2TZkyhVK6cOHCNWvWyN0uz4uPj8/JybFYLH5+fpTSs2fPDho0SO5Ged7ixYv/+te/UkrHjx9/8OBBURTj4uJyc3PlbpeHXbhwYeDAgZTSbdu2TZ8+nVK6YMGC9evXy9ysZhAXF5eXl2cwGIKCgiilp0+fHjJkiNyN8gzMgN1x+/btuLg4o9EoiqLVak1MTLx27ZrcjfK8nJycjh07EkKMRqPZbOY4LiEhQXmPIeXk5MTFxRFCjEajyWQihCjyglJK8/LyOnToYDQa7Xa7w+FQZDdJfeO2a9euN27ckLtdHuYj41YQhKKiotjYWKPRKJ0IraRuYhOW68RmigAAAclJREFUOxITEw8dOmQwGCIiIg4cOMDzfO/eveVulOclJiamp6cnJSXdvHkzLS3tiSeeuHz5cs+ePeVul4clJiZmZGQUFhYeOnTo1q1bhYWFx48fT0pKkrtdHibFobS0tNLS0rCwsIMHD1qtVqWO2yNHjvTt2zc7O/vQoUNJSUlXr15V3i7oxMTEb775pqio6PDhw7m5uUVFRcePHx8xYoTc7fIwnuc7deqUnp6em5sbGhqalpam0+mUM27lnoJ7pWPHjkVHR/fu3TsrK6tbt24dOnQ4e/as3I3yvLKyskGDBkm/rKdNmxYaGiqtSCvPq6++GhIS8vLLL3/++eehoaGjR4+urq6Wu1Ged+TIkTZt2vTp0yczM7NLly4dO3a8cOGC3I3yvJKSkgEDBoSHhx8+fHjy5MmhoaHSirTyzJ8/Pzg4+Pe///1nn33WqlWrsWPHGo1GuRvleYcOHYqKinr44YczMzPj4+M7d+6clZUld6M8A7ugAQAAZIB7wAAAADJAAAYAAJABAjAAAIAMEIABAABkgAAMAAAgAwRgAAAAGSAAAwAAyAABGAAAQAYIwAAAADJAAAYAAJABAjAAAIAMEIABAABk8P8AR/bE+AkR63EAAAAASUVORK5CYII="

}

}

getConstructorPlanId
--------------------

метод

описание

Возвращает id тарифного плана конструктора VPS по значениям кол-ва ядер, ОЗУ, объема диска и категории

возвращаемое значение

id тарифного плана конструктора VPS

параметры в запросе

cpu\_cores

integer

кол-во ядер CPU

ram

integer

ОЗУ в гигабайтах

volume\_disk

integer

жесткий диск в гигабайтах

category\_id

integer

id категории

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getConstructorPlanId"

"params":{

"cpu\_cores":

4

"ram":

2

"volume\_disk":

20

"category\_id":

1

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"215748354293096.RsEbKmyyev"

"result":

124

}

changePlan
----------

метод

описание

Изменение тарифного плана

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

planId

integer

ID Тарифного плана

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"changePlan"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"vpsPlanId":

4

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"851409313888159.HbxZlMeGbp"

"result":

1

}

powerOn
-------

метод

описание

Включение VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"powerOn"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"528007144710978.bNOgcSCJoi"

"result":

1

}

powerOff
--------

метод

описание

Выключение VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"powerOff"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"217824748450948.yQwudBniRK"

"result":

1

}

reboot
------

метод

описание

Перезагрузка VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"reboot"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"339045769301497.hztDCuXaoZ"

"result":

1

}

getCurrentAction
----------------

метод

описание

Получение текущей операции по VPS

возвращаемое значение

получение текущей операции по VPS

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

string

пример запроса

{

"jsonrpc":

"2.0"

"method":

"getCurrentAction"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"460594474260523.tDneBAxcGv"

"result":

"start"

}

reinstallOs
-----------

метод

описание

Переустановка образа VPS

возвращаемое значение

1 - успешно, 0 - ошибка

параметры в запросе

billingId

string

идентификатор машины

distributiveId

integer

ID Дистрибутива

тип данных в ответе

integer

пример запроса

{

"jsonrpc":

"2.0"

"method":

"reinstallOs"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

"distributiveId":

32

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"067069631845647.QceVobaWre"

"result":

1

}

logs
----

метод

описание

Получение логов операций

возвращаемые значения в свойствах элементов массива

'type' string тип операции

'status' string статус операции

'started\_at' string дата и время начала операции в формате YYYY-MM-DD HH:MM:SS

'ended\_at' string дата и время окончания операции в формате YYYY-MM-DD HH:MM:SS

параметры в запросе

billingId

string

идентификатор машины

тип данных в ответе

array

пример запроса

{

"jsonrpc":

"2.0"

"method":

"logs"

"params":{

"billingId":

"vhp\*\*\*\*\_vps\_1"

}

}

пример ответа

{

"jsonrpc":

"2.0"

"id":

"064408096436268.ZppnSghsvf"

"result":\[

{

"type":

"Старт"

"status":

"Завершена"

"started\_at":

"2023-03-15 13:42:03"

"ended\_at":

"2023-03-15 13:43:03"

}

{

"type":

"Стоп"

"status":

"Завершена"

"started\_at":

"2023-03-15 13:40:02"

"ended\_at":

"2023-03-15 13:41:03"

}

{

"type":

"Создание бэкапа"

"status":

"Завершена"

"started\_at":

"2023-03-13 16:10:02"

"ended\_at":

"2023-03-13 16:11:03"

}

{

"type":

"Удаление бэкапа"

"status":

"Завершена"

"started\_at":

"2023-03-13 16:04:02"

"ended\_at":

"2023-03-13 16:05:03"

}

{

"type":

"Создание бэкапа"

"status":

"Завершена"

"started\_at":

"2023-03-13 15:49:02"

"ended\_at":

"2023-03-13 15:50:03"

}

{

"type":

"Создание"

"status":

"Завершена"

"started\_at":

"2023-03-13 15:14:03"

"ended\_at":

"2023-03-13 15:15:05"

}

\]

}

#### Стань партнером

Выгодное предложение SpaceWeb:

*   до 48% вознаграждение ежемесячно,
*   быстрая оплата на карту,
*   работа по договору.

[Подробнее](https://sweb.ru/partner/)

Услуги

*   [Хостинг сайтов](https://sweb.ru/hosting/)
*   [Облачные серверы](https://sweb.ru/cloud/vps/)
*   [VPS/VDS](https://sweb.ru/vds/)
*   [Регистрация доменов](https://sweb.ru/domains/)
*   [Конструктор сайтов](https://sweb.ru/site-constructor/)
*   [Аренда серверов](https://sweb.ru/servers/)
*   [SSL-сертификаты](https://sweb.ru/ssl/)
*   [Лицензии на CMS](https://sweb.ru/cms/)

Полезное

*   [Whois сервис](https://sweb.ru/whois/)
*   [Бесплатный хостинг](https://sweb.ru/hosting/free/)
*   [Дешевый хостинг](https://sweb.ru/hosting/cheap/)
*   [Бесплатный VPS](https://sweb.ru/vds/free/)
*   [Дешевый VPS](https://sweb.ru/vds/cheap/)
*   [Акции и бонусы](https://sweb.ru/web/)
*   [API SpaceWeb](https://apidoc.sweb.ru/)
*   [РБК: главные новости России и мира](https://www.rbc.ru/)
*   [Свежие новости компаний](https://companies.rbc.ru/)
*   [РБК Инвестиции: котировки](https://www.rbc.ru/quote)
*   [Курсы по программированию и IT](https://www.rbc.ru/courses/programming)

Решения

*   [Docker](https://sweb.ru/vds/docker/)
*   [Node.js](https://sweb.ru/vds/nodejs/)
*   [GitLab](https://sweb.ru/vds/gitlab/)
*   [NextCloud](https://sweb.ru/vds/nextcloud/)
*   [Rocket.Chat](https://sweb.ru/vds/rocketchat/)
*   [ispmanager](https://sweb.ru/vds/isp/)
*   [BitrixVM](https://sweb.ru/vds/bitrix/)
*   [VPS на Linux](https://sweb.ru/vds/linux/)
*   [Все решения](https://sweb.ru/vds/apps/)

О компании

*   [О компании SpaceWeb](https://sweb.ru/company/)
*   [Отзывы клиентов](https://sweb.ru/reviews/)
*   [Новости компании](https://sweb.ru/news/)
*   [Бортовой журнал](https://journal.sweb.ru/)
*   [Контакты](https://sweb.ru/contactinfo/)
*   [Вакансии](https://sweb.ru/vacancies/)

Поддержка

*   [Вопросы и ответы](https://help.sweb.ru/)
*   [Способы оплаты](https://sweb.ru/pay/)
*   [Реквизиты](hhttps://sweb.ru/contact/properties/)

Скачать приложение

*   [![googlePlayDownload](//s.sweb.ru/img/google_play.svg)](https://play.google.com/store/apps/details?id=ru.sweb.app&hl=ru)
*   [![appleStoreDownload](//s.sweb.ru/img/app_store.svg)](https://apps.apple.com/ru/app/spaceweb-%D1%85%D0%BE%D1%81%D1%82%D0%B8%D0%BD%D0%B3/id1583597572)

[Политика конфиденциальности](https://sweb.ru/docs/site_policy.pdf)[Правила](https://sweb.ru/support/rules/)[Политика обработки персональных данных](https://sweb.ru/docs/personal_data.pdf)[Оферты и документы](https://sweb.ru/documents/)

*   [+7 (812) 209-41-49](tel:+78122094149) (в Санкт-Петербурге),
*   [+7 (495) 109-41-49](tel:+74951094149) (в Москве),
*   [8 (800) 777-86-49](tel:88007778649) (бесплатно по России)

*   [![SpaceWeb В Контакте](https://s.sweb.ru/img/icons/icon_vk.svg)](https://vk.com/spaceweb_ru)
*   [![Telegram](https://s.sweb.ru/img/icons/icon_telegram.svg)](https://t.me/spaceweb)

© 2001-2026 ООО «СпейсВэб» Все права защищены.

Общество с ограниченной ответственностью «СпейсВэб». Адрес юридического лица: 197046, г. Санкт-Петербург, вн.тер.г. муниципальный округ Посадский, ул. Чапаева, д. 15 литера А, помещ. 1-Н, офис А-105.[Адрес офиса](https://sweb.ru/contact/properties/): 197046, Санкт-Петербург, ул. Чапаева, д. 15, лит. А, 1 этаж, офис А-105.

Электронный адрес для направления юридически значимых сообщений и заявлений о нарушении авторских и (или) смежных прав: [feedback@sweb.ru](mailto:feedback@sweb.ru). Настоящий ресурс может содержать материалы 18+.

Платформа управления облачными сервисами, услугами и хостингом SpaceWeb включена в реестр российского ПО.[Запись №30259 от 22.10.2025.](https://reestr.digital.gov.ru/reestr/4119475/) Права на использование Платформы предоставляются по модели SaaS (Software as a Service) посредством удаленного доступа к Платформе через информационно-телекоммуникационную сеть Интернет.