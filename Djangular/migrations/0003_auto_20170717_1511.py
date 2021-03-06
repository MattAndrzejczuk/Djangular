# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djangular', '0002_auto_20170717_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangularmasterviewcontroller',
            name='djangular_directive',
            field=models.ManyToManyField(blank=True, null=True, to='Djangular.DjangularDirective'),
        ),
        migrations.AlterField(
            model_name='djangularmasterviewcontroller',
            name='djangular_service',
            field=models.ManyToManyField(blank=True, null=True, to='Djangular.DjangularService'),
        ),
        migrations.AlterField(
            model_name='djangularmasterviewcontroller',
            name='djangular_slave_vc',
            field=models.ManyToManyField(blank=True, null=True, to='Djangular.DjangularSlaveViewController'),
        ),
        migrations.AlterField(
            model_name='djangularmasterviewcontroller',
            name='module_js',
            field=models.TextField(default="(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME', ['flow']).config(config); \n\n\tfunction config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) { \n\t$stateProvider\n\t.state('app.FUSE_APP_NAME', { \n\t\turl: '/FUSE_APP_NAME', \n\t\tviews: { \n\t\t\t'content@app': { \n\t\t\t\ttemplateUrl: '/dynamic_lazarus_page/DynamicHTMLInjector/?name=FUSE_APP_NAME', \n\t\t\t\tcontroller: 'FUSE_APP_NAMEController as vm'\n\t\t\t}\n\t\t} \n\t})  \n\t_DJANGULAR_SLAVE_VC_INJECTION_POINT_; /* Djangular Slave VCs automatically injected here. */ \n\tmsNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', { \n\t\ttitle: 'FUSE_APP_TITLE', \n\t\ticon: 'FUSE_APP_ICON', \n\t\tstate: 'app.FUSE_APP_NAME', \n\t\tweight: 3 \n\t});    \n\t} \n})();"),
        ),
    ]
