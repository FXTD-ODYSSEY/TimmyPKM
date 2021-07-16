@echo off
explorer "http://localhost:8080"
set TIDDLYWIKI_PLUGIN_PATH=%~dp0Plugins
tiddlywiki IndexWiki --server 8080 