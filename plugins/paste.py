from disco.bot import Plugin
from plugins.paster import Paster

paster = Paster()

languages = ['1c', 'abnf', 'accesslog', 'actionscript', 'ada', 'angelscript', 'apache', 'applescript', 'arcade', 'arduino', 'armasm', 'asciidoc', 'aspectj', 'autohotkey', 'autoit', 'avrasm', 'awk', 'axapta', 'bash', 'basic', 'bnf', 'brainfuck', 'cal', 'capnproto', 'ceylon', 'clean', 'clojure', 'clojure-repl', 'cmake', 'coffeescript', 'coq', 'cos', 'cpp', 'crmsh', 'crystal', 'cs', 'csp', 'css', 'd', 'dart', 'delphi', 'diff', 'django', 'dns', 'dockerfile', 'dos', 'dsconfig', 'dts', 'dust', 'ebnf', 'elixir', 'elm', 'erb', 'erlang', 'erlang-repl', 'excel', 'fix', 'flix', 'fortran', 'fsharp', 'gams', 'gauss', 'gcode', 'gherkin', 'glsl', 'gml', 'go', 'golo', 'gradle', 'groovy', 'haml', 'handlebars', 'haskell', 'haxe', 'hsp', 'htmlbars', 'http', 'hy', 'inform7', 'ini', 'irpf90', 'isbl', 'java', 'javascript', 'jboss-cli', 'json', 'julia', 'julia-repl', 'kotlin', 'lasso', 'ldif', 'leaf', 'less', 'lisp', 'livecodeserver', 'livescript', 'llvm', 'lsl', 'lua', 'makefile', 'markdown', 'mathematica', 'matlab', 'maxima', 'mel', 'mercury', 'mipsasm', 'mizar', 'mojolicious', 'monkey', 'moonscript', 'n1ql', 'nginx', 'nimrod', 'nix', 'nsis', 'objectivec', 'ocaml', 'openscad', 'oxygene', 'parser3', 'perl', 'pf', 'pgsql', 'php', 'pony', 'powershell', 'processing', 'profile', 'prolog', 'properties', 'protobuf', 'puppet', 'purebasic', 'python', 'q', 'qml', 'r', 'reasonml', 'rib', 'roboconf', 'routeros', 'rsl', 'ruby', 'ruleslanguage', 'rust', 'sas', 'scala', 'scheme', 'scilab', 'scss', 'shell', 'smali', 'smalltalk', 'sml', 'sqf', 'sql', 'stan', 'stata', 'step21', 'stylus', 'subunit', 'swift', 'taggerscript', 'tap', 'tcl', 'tex', 'thrift', 'tp', 'twig', 'typescript', 'vala', 'vbnet', 'vbscript', 'vbscript-html', 'verilog', 'vhdl', 'vim', 'x86asm', 'xl', 'xml', 'xquery', 'yaml', 'zephir']

class Paste(Plugin):
    @Plugin.listen('MessageCreate')
    def on_message_create(self, event):
        split_msg = str(event.message.content).split(' ')
        if len(split_msg) == 1 and split_msg[0] == '$paste':
            event.reply('Usage: $paste <language/plaintext> <text to post>')
        else:
            command = split_msg[0]
            language_assump = split_msg[1]
            was_right = False
            if any(x in language_assump for x in languages):
                was_right = True
                language = language_assump
            else:
                language = "plaintext"
            if command != '$paste':
                pass
            else:
                if was_right:
                    result = paster.paste_text(str(' '.join(split_msg[2:])).replace('```', ''), language=language)
                else:
                    result = paster.paste_text(str(' '.join(split_msg[1:])).replace('```', ''), language=language)
                print(result)
                event.message.delete()
                if 'https://' in result:
                    event.reply('{} here is your psty.io link: {}'.format(event.member.user.mention, result))
                else:
                    event.reply('{}, Sorry there was an issue uploading that!'.format(event.member.user.mention))
