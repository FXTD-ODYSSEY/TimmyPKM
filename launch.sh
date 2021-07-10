baseDirForScriptSelf=$(cd "$(dirname "$0")"; pwd)
export TIDDLYWIKI_PLUGIN_PATH=$baseDirForScriptSelf/Plugins  
# echo $TIDDLYWIKI_PLUGIN_PATH
tiddlywiki +plugins/linonetwo/watch-fs IndexWiki --server 8080 