import discord
#import discord.Intents
import random
import base64
import cow
import time
import requests
import json
from discord.ext import commands
from discord.utils import get
from datetime import datetime #new
from discord.ext.commands import has_permissions, MissingPermissions

__version__=2

def base64it(text):
    text_bytes=text.encode('ascii')
    text_b64_bytes=base64.b64encode(text_bytes)
    text_b64=text_b64_bytes.decode('ascii')
    return text_b64

intents=discord.Intents.default()
intents.members=True
client=commands.Bot(command_prefix='x!', intents=intents)

@client.event
async def on_ready():
    print('I am up!')
    channel=client.get_channel(735167054247886988)
    link= await channel.create_invite()
    await channel.send('Kindly !d bump whenever possible! Thanks!')
    await client.change_presence(activity=discord.Game(name=f'x!help on Gateway.\n{link}'))
    with open('log.txt','w+') as file: #new
        file.write(f'Booted up again at: {datetime.now()}') #new

@client.event
async def on_member_join(member):
    id1="secret"
    challenge=f"Flag({id1})"

    channel=client.get_channel(768528739986309152)
    guild=client.get_guild(735163958356607077)
    user=client.get_user(484724246308716544)

    await channel.send(f'''Welcome {member.mention} to Gateway! Thanks to you Gateway has {guild.member_count} members! You are requested to decode the following string to and verify that you can be let in. This is a way to make sure that Gateway has quality members: 

`{base64it(challenge)}`

[Everyone's String is unique, So please just decode your own ^^]

If some error occurs then do `challenge` To get the string again. And if you're a newbie and this seems very confusing to you, then feel free to dm a mod or {user.name}#{user.discriminator}''')
    if member.dm_channel==None:
        await member.create_dm()
    await member.dm_channel.send(f"Welcome to Gateway! Kindly proceed to #firewall and verify yourself there to gain access to the server. Please Follow the discord TOS. That's really it. Have fun, make loads of friends ^^ and stay curious. This community is filled with cybersecurity professionals, tech enthusiasts, Programmers and nerds. Go to the server and maybe introduce yourself <3")

@client.event
async def on_message(message):
    channel=client.get_channel(768528739986309152)
    if message.channel==channel:
        member=message.author
        id1="secret"
        challenge=f"Flag({id1})"
        if(message.content.lower()==challenge.lower() or message.content==str(id1) or challenge.lower() in message.content.lower()):
            await message.channel.send(f'Welcome in {message.author.mention}! Go to general and introduce yourself to the community now!')
            await message.delete()
            channel=client.get_channel(765239910621249547)
            role=get(message.guild.roles, name="member")
            await message.author.add_roles(role)
        elif(message.content==base64it(challenge)):
            await message.channel.send(f'um that\'s what i asked you to decode, yes?')
        elif(message.content.lower()=='challenge'):
            await message.channel.send(f"{message.author.mention} Your string to decode is `{base64it(challenge)}`")
        elif('hard' in message.content.lower()):
            if message.author==client.user:
                return
            elif len(message.author.roles)==1 or len(message.author.roles)==2:
                    await message.channel.send(f"{message.author.mention} it's okay if you find it hard fam. just message a mod/admin or elliot :))")

        elif('base64' in message.content.lower()):
            await message.delete()

    elif message.content.lower()=='d4vid' or message.content.lower()=='david':
        emoji=client.get_emoji(767666777387696129)
        await message.add_reaction(emoji)

    elif message.content.lower()=="spore":
        emoji=client.get_emoji(768054301074653214)
        await message.add_reaction(emoji)
    
    stuff=message.content.lower()

    if message.channel==message.channel:
        if "unknowncheats.me" in stuff:
            await message.delete()
            await message.channel.send(f"{message.author.mention} you have been warned for using a link that has been banned. Excessive usage will lead to a mute or a ban.")

        elif "exploit.in" in stuff:
            await message.delete()
            await message.channel.send(f"{message.author.mention} you have been warned for using a link that has been banned. Excessive usage will lead to a mute or a ban.")

        elif "redirecthost.online" in stuff:
            emoji=client.get_emoji(767676277104050176)
            await message.add_reaction(emoji)
            #await message.delete()
            #await message.channel.send(f"{message.author.mention} you have been warned for using a link that has been banned. Excessive usage will lead to a mute or a ban.")


    await client.process_commands(message)

#----General Use Commands-----

@client.command(pass_context=True)
async def invite(ctx):
    link=await ctx.channel.create_invite()
    await ctx.send(f"Here is our invite link: {link} {ctx.message.author.mention}")
    channel=client.get_channel(765630153631596574)
    await channel.send(f"{ctx.message.author.mention} Created an Invite.")

@client.command(pass_context=True, aliases=['cowsay'])
async def cowsay_(ctx, *, text):
    text=text.replace('`','')
    cowsay_text=cow.cowsay(text)
    await ctx.channel.send(f"```{cowsay_text}```")

@client.command(pass_context=True,aliases=['skid','ill','i','I'])
async def illegal(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("Alright kiddo stop right there. Enough messing around. **What you're talking about seems to be illegal or against the TOS of Discord.** This is a \"WhiteHat Server\" and we don't appreciate the intentions you are reflecting. Kindly refrain from talking about whatever you are talking about or this could lead to a warning, mute or ban itself without any warning. Again, We don't want to be yeeted off of discord. Be careful. Thanks.")
    msg=ctx.message
    await msg.delete()
    channel=get_channel(765630153631596574)
    await channel.send(f"{ctx.message.author.mention} Used `x!illegal`")

@client.command(pass_context=True, aliases=['howtostart','s'])
async def start(ctx):
    msg=ctx.message
    await msg.delete()
    steps='''So you want to get into hacking but you are confused as to where to begin? Here is what I recommend:
1. __**Effort:**__ Effort is necessary anywhere. I recommend that you start reading up about things constantly.
2. __**Be curious:**__ Be fucking curious about everything!
3. __**Google is your fuck buddy:**__ A person I respected and idiolized back in my skid days told me that. It simply means
that you should Google EVERYTHING you can. Indeed there are things that you won't understand. But try can do is try your best to understand it. Slam your head against it for time maybe kek.
4. __**Pick up a coding Language:**__ Programming is important in hacking. I mean you CAN hack without knowing how to code but it limits you and you would have a harder time with things. You can pick up any programming language that you prefer. Python, C++, C# or Javascript etc. If you're worried about how to pick that up, I have a whole article dedicated to just that here: 

<https://medium.com/@0x0elliot/how-to-learn-your-first-programming-language-to-get-into-hacking-2112d9885025>

5. __**Get into infosec communities:**__ This is equally as important. If you're the smartest person in the room, then you are in the wrong room. Find yourself a place where you aren't the smartest. Accept your flaws and grow there. Besides Gateway itself, I can recommend you some great communities you can join:
'''
    steps2='''Good Cybersecurity/Infosec servers with smart people and a non-toxic community where you can grow in given that you aren't ego filled and are always humble: 

LHC: https://discord.gg/bavNVtP
Crow's Nest: https://discord.gg/tMRrYzd

LHC has some great resources and a whole proper website. You can check that there as well.

Good Programming server to join where you will get help related to your programming queries:

Coding Support: https://discord.gg/Nsf7SdZ

Honestly, I will always give these guys a shoutout. I genuinely think that this is a great community. Coding Support server always ends up helping me.

6. __**CTFs, CTFs, CTFs:**__ Can't stress this enough. CTFs will teach you a lot. There are a lot CTFs you can do. Just don't run away from them. Keep trying. It's okay to see the solutions to your CTFs sometimes, Especially initially. 

CTFs I recommend for absolute beginners:
 
The ones at LHC [I love this server] kek (The CTFs go from easy to Hard as you solve each chronologically. I still haven't completed Unsanitary :( )
The Crypto ones and initial RE ones at Crow's Nest
Hacker101: <https://www.hacker101.com/>
PicoCTF: <https://picoctf.com/>

Watch some liveoverflow beginner videos to understand the basics of hacking. Look that up on youtube. 
https://www.youtube.com/watch?v=Lus7aNf2xDg

^ here liveoverflow explains how to learn hacking with CTFs. Though do this after you have picked up some basic hacking from the other CTFs and you know some programming.

These are the ones that I found useful in my rookie days. I would recommend looking into bug bounties and trying to find and report vulnerabilities. It helps you formulate an approach of your own. Infact the LHC CTFs are perfect in helping you do just do that. Best of luck!
'''
    user=ctx.message.author
    if user.dm_channel==None:
        await user.create_dm()
    await user.dm_channel.send(steps)
    await user.dm_channel.send(steps2)
    channel=client.get_channel(765630153631596574)
    await channel.send(f"{user.mention} Used `x!start` Command")

@client.command(pass_context=True)
async def count(ctx):
    await ctx.send(f"{ctx.message.guild.name} Has **{ctx.message.guild.member_count}** members!")


#--CTF Team only commands---

@client.command(pass_context=True)
@commands.has_role('CTF Team')
async def newctf(ctx):
    ts=int(time.time()//1)
    limit=1
    link=f"https://ctftime.org/api/v1/events/?limit={limit}&start={ts}"
    headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    
    r=requests.get(link,headers=headers)
    webhook="webhook"
    res=r.json()[0]

    organiser=(res['organizers'])[0]["name"].replace('@','attheratesymbol')
    onsite=res['onsite']
    description=res['description'].replace('@','attheratesymbol')
    finish=res['finish']
    format_=res['format'].replace('@','attheratesymbol')
    duration=res['duration']
    title=res['title']
    participants=res['participants']
    url=res['url']
    url_ctftime=res['ctftime_url']
    content=f'**{title}: {url}\nOnsite: {onsite}\nStyle: {format_}\nduration: {duration}\nNumber of participants: {participants}\nfinishes on: {finish}\nCTF time URL: {url_ctftime}\nDescription:** {description}'

    data={'content':content}
    q=requests.post(webhook,data=data)
    await ctx.message.delete()

#-----Administrator commands------

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def chstatus(ctx, *, status):
    if status=='default':
        await client.change_presence(activity=discord.Game(name=f'x!help At Gateway'))
    await client.change_presence(activity=discord.Game(name=f"{status}"))
    await ctx.send(f"Status changed to: {status}")

@client.command(pass_context=True)
@has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason):
    print(reason)
    msg=f'Well rip {user.mention} you got banned for **Reason:** {reason}'
    if user.dm_channel==None:
        await user.create_dm()
    await user.dm_channel.send(content=f"You were banned from Gateway By {ctx.message.author.mention}for Reason: {reason}")
    await ctx.send(msg)
    await user.ban(reason=reason)
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def kick(ctx, user:discord.Member,*, reason):
    msg=f'Well rip {user.mention} was kicked for **Reason:** {reason}'
    if user.dm_channel==None:
        await user.create_dm()
    await user.dm_channel.send(content=f"You were kicked from Gateway by {ctx.message.author.mention} for Reason: {reason}")
    await ctx.send(msg)
    await user.kick(reason=reason)
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(ban_members=True)
async def findbans(ctx):
    banned_users=await ctx.message.guild.bans()
    user=ctx.message.author
    if user.dm_channel==None:
        await user.create_dm()
    info=f"Banned member info: "
    for ban in banned_users:
        info+=f"\n{ban}\n"
    await user.dm_channel.send(f"{info}")
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(manage_roles=True)
async def hidden(ctx, member:discord.Member):
    role=get(ctx.guild.roles, name='hidden')
    await member.add_roles(role)
    if member.dm_channel==None:
        await member.create_dm()
    await member.dm_channel.send(f"You have been silently given the hidden role giving you access to the hidden chat by a mod.")
    channel=client.get_channel(765630153631596574)
    await channel.send(f'{ctx.message.author.mention} Gave {member.mention} The **hidden** role.')
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(manage_roles=True)
async def unhidden(ctx, member:discord.Member):
    role=get(ctx.guild.roles, name='hidden')
    await member.remove_roles(role)
    if member.dm_channel==None:
        await member.create_dm()
    await member.dm_channel.send(f"Your hidden role has now been taken away")
    channel=client.get_channel(765630153631596574)
    await channel.send(f'{ctx.message.author.mention} Took away {member.mention}\'s **hidden** role.')
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def toxic(ctx, member:discord.Member):
    role=get(ctx.guild.roles, name="Toxic")
    await member.add_roles(role)
    await ctx.channel.send(f"{member.mention} You have been given the `Toxic` Role which only limits you to the brig, by a mod.")
    if member.dm_channel==None:
        await member.create_dm()
    await member.dm_channel.send(f"You have been given the `Toxic` Role which restricts your access to the server. Contact a mod if you feel like this isn't a right decision.")
    channel=client.get_channel(765630153631596574)
    await channel.send(f"{member.mention} Got the `Toxic` Role from {ctx.message.author.mention}")
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def untoxic(ctx, member:discord.Member):
    role=get(ctx.guild.roles, name="Toxic")
    await member.remove_roles(role)
    await ctx.channel.send(f"{member.mention} Had their `Toxic` Role removed.")
    if member.dm_channel==None:
        await member.create_dm()
    await member.dm_channel.send(f"Your `Toxic` Role has been removed. Now you have full access to the server.")
    channel=client.get_channel(765630153631596574)
    await channel.send(f"{member.mention} Got the `Toxic` Role **REMOVED** from {ctx.message.author.mention}")
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def mute(ctx, member:discord.Member):
    role=get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.channel.send(f"{member.mention} was muted. Please calm the fuck down now.")
    if member.dm_channel==None:
        await member.create_dm()
    await member.dm_channel.send(f"You have been muted in Gateway. You are requested to behave. If you feel like this wasn't just then feel free to message the elliot or a staff appealing to be unmuted.")
    msg=ctx.message
    await msg.delete()
    channel=client.get_channel(765630153631596574)
    await channel.send(f'User {member.mention} has been muted by {ctx.message.author.mention}')

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def unmute(ctx, member:discord.Member):
    role=get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.channel.send(f'User {member.mention} has been unmuted.')
    if member.dm_channel==None:
        await member.create_dm()
    await member.dm_channel.send(f'You have been unmuted in Gateway. Enjoy!')
    channel=client.get_channel(765630153631596574)
    await channel.send(f"user {member.mention} has been unmuted by {ctx.message.author.mention}")
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def warn(ctx, user:discord.Member, *, reason):
    await ctx.send(f"{user.mention} has been warned and politely asked to calm the fuck down By a mod for **{reason}**")
    if user.dm_channel==None:
        await user.create_dm()
    await user.dm_channel.send(content=f'You have been warned by {ctx.message.author.mention} to calm the fuck down because of the reason: **{reason}**')
    channel=client.get_channel(765630153631596574)
    await channel.send(f"{ctx.message.author.mention} **WARNED** {user.mention} FOR **{reason}**")
    msg=ctx.message
    await msg.delete()
    msg=ctx.message

@client.command(pass_context=True)
@has_permissions(manage_nicknames=True)
async def chnick(ctx, member:discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f"{member.mention} your nickname was changed to `{nick}` by a mod.")
    channel=client.get_channel(765630153631596574)
    await channel.send(f"{member.mention} Got their nick name changed by a mod.")
    msg=ctx.message
    await msg.delete()

@client.command(pass_context=True)
@has_permissions(manage_messages=True)
async def purge(ctx,arg):
    limit=int(arg)
    msg=ctx.message
    await msg.delete()
    await ctx.channel.purge(limit=limit)
    channel=client.get_channel(765630153631596574)
    await channel.send(f"{ctx.message.author.mention} Purged {limit} messages")

token="oof"
client.run(token)
