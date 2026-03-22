![FROST RAID BOT](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHY5_AqNmhdbrdTzMbXAjqLPuldy6cGNvuFw&s)

# FROST RAID BOT

Bot automatizado avançado para operações de raid em servidores Discord com menu interativo de 90 funções.

## Configuração

1. Obtenha um token de bot do Discord em https://discord.com/developers/applications
2. Substitua o token no arquivo main.py pelo seu token
3. Configure as permissões necessárias para o bot (Administrador)
4. Ative todas as Privileged Gateway Intents no Developer Portal

## Instalação

Instale as dependências:
```
pip install -r requirements.txt
```

Dependências necessárias:
```
discord.py
aiohttp
```

## Como usar

Execute o bot:
```
python main.py
```

### Comandos

- `!menu`: Abre o menu interativo com 90 funções de raid no seu DM

## Sistema de Menu Interativo

O bot possui um menu de 3 páginas com 90 funções diferentes:

### Navegação
- Digite o número da função desejada (1-90)
- Digite `next` para avançar para a próxima página
- Digite `back` para voltar para a página anterior
- Digite `99` para executar AUTO RAID (todas as funções principais)

### Página 1 (1-30) - Funções Básicas
- Nuke Complete, Create Channels, Spam Channels
- Webhook Spam, Kick/Ban All, Create Roles
- Get Admin, Change Server, DM All
- Delete Emojis, Mass Mention, Spam Reactions
- Delete Roles, Rename Members, Mass Nick
- Create Threads, Delete Webhooks, Spam Voice
- Remove Invites, Clear Messages, Pin Spam
- Create Categories, Rename Channels, Timeout All
- Server Template, Spam Events, Forum Spam
- Remove Integrations, Max Channels

### Página 2 (31-60) - Funções Intermediárias
- Max Roles, Delete Stickers, Deafen/Mute All
- Disconnect Voice, Spam Stage Channels, Clone Server
- Mass Unban, Spam Invites, Create Forums
- Role Spam, Lock Channels, Remove Reactions
- Spam Embeds, Change Region, Create Emojis
- Slowmode Max/Off, Thread Spam, Archive Threads
- Purge All, Typing Spam, Edit Messages
- Role Colors, Channel Topics, Spam Nicks
- Banner/Splash Spam, Remove Discovery, Disable Community

### Página 3 (61-90) - Funções Avançadas
- Remove Verification, Delete Rules, Announcement Spam
- Disable AutoMod, Remove Welcome, Remove Boosts
- Prune Members, Mass Move Voice, Voice Spam
- Disable Widget, Forum Tags Spam, Archive All
- Notification Spam, Reaction Spam, Remove Safety
- Region Spam, AFK Spam, System Msg Spam
- **[90] TOTAL DESTRUCTION** - Executa todas as funções simultaneamente

## Funcionalidades Principais

### Destruição de Servidor
- Exclusão automática de todos os canais (texto, voz, stage, fóruns)
- Exclusão automática de todos os cargos
- Remoção de emojis, stickers e integrações
- Alteração completa das configurações do servidor

### Criação em Massa
- Criação de até 500 canais de texto
- Criação de até 250 cargos personalizados
- Criação de canais de voz e stage
- Criação de categorias e fóruns

### Spam e Flooding
- Spam de mensagens com @everyone em todos os canais
- Webhook spam para bypass de rate limits
- Spam de convites, embeds, reações
- Spam de DMs para todos os membros

### Controle de Membros
- Ban/Kick em massa
- Timeout de 28 dias para todos
- Rename/Nick change em massa
- Deafen/Mute em canais de voz
- Prune de membros inativos

### Modificação de Servidor
- Alteração de nome, ícone, banner, splash
- Mudança de região, configurações de verificação
- Remoção de recursos comunitários
- Desativação de AutoMod e widgets

## Recursos Técnicos

- **Execução Assíncrona**: Todas as funções rodam simultaneamente para máxima velocidade
- **Sistema de Tasks**: Uso de asyncio.create_task para paralelização
- **Tratamento de Erros**: Try-catch em todas as operações críticas
- **Rate Limit Bypass**: Uso de webhooks e delays estratégicos
- **Menu DM**: Sistema de navegação por páginas com sessões de usuário
- **Status Personalizado**: "Assistindo /cybersec"

## Funções Especiais

### [99] AUTO RAID
Executa automaticamente:
- Deletar todos os canais
- Deletar todos os cargos
- Enviar DM em massa
- Alterar servidor (nome, ícone)
- Criar 200 cargos
- Criar 500 canais
- Banir todos os membros
- Deletar emojis

### [90] TOTAL DESTRUCTION
Executa simultaneamente todas as funções de destruição para devastação completa do servidor.

## Links Incluídos

- Discord: https://discord.gg/WJ76QgRA
- Repositório: [Adicione seu link aqui]

## Avisos Legais

⚠️ **IMPORTANTE**: Este bot foi desenvolvido exclusivamente para fins educacionais e de teste em servidores próprios onde você possui autorização explícita.

- O uso deste bot em servidores sem permissão é ILEGAL
- Viola os Termos de Serviço do Discord
- Pode resultar em banimento permanente da plataforma
- Pode ter consequências legais dependendo da jurisdição
- Desenvolvedores não se responsabilizam pelo uso indevido

**Use apenas em servidores de teste próprios.**

## Créditos

FROST RAID BOT V0.0.0
Desenvolvido por: FROST 

---

*Para suporte ou dúvidas, entre em nosso Discord: https://discord.gg/AAnFNAawqA*